-- 1. In Supabase, open SQL Editor and run this file.
-- 2. In supabase-config.js, replace the URL and publishable key placeholders.
--    Use the project's publishable (or legacy anon) key, never its service_role key.
-- 3. Redeploy the static site. Ratings and comments are public to site visitors.

create table if not exists public.project_ratings (
  voter_id uuid primary key,
  rating smallint not null check (rating between 1 and 5),
  updated_at timestamptz not null default now()
);

alter table public.project_ratings enable row level security;

create or replace function public.get_project_rating_summary()
returns table (average_rating numeric, rating_count bigint)
language sql
stable
security definer
set search_path = ''
as $$
  select
    coalesce(round(avg(rating)::numeric, 1), 0::numeric),
    count(*)::bigint
  from public.project_ratings;
$$;

create or replace function public.submit_project_rating(p_voter_id uuid, p_rating smallint)
returns void
language plpgsql
security definer
set search_path = ''
as $$
begin
  if p_voter_id is null or p_rating is null or p_rating not between 1 and 5 then
    raise exception 'A voter ID and a rating from 1 to 5 are required.';
  end if;

  insert into public.project_ratings (voter_id, rating)
  values (p_voter_id, p_rating)
  on conflict (voter_id) do update
    set rating = excluded.rating, updated_at = now();
end;
$$;

revoke all on function public.get_project_rating_summary() from public;
revoke all on function public.submit_project_rating(uuid, smallint) from public;
grant execute on function public.get_project_rating_summary() to anon, authenticated;
grant execute on function public.submit_project_rating(uuid, smallint) to anon, authenticated;

create table if not exists public.project_comments (
  id uuid primary key default gen_random_uuid(),
  name text not null default 'Anonymous' check (char_length(name) <= 40),
  body text not null check (char_length(btrim(body)) between 1 and 500),
  created_at timestamptz not null default now()
);

create index if not exists project_comments_created_at_idx
  on public.project_comments (created_at desc);

alter table public.project_comments enable row level security;

drop policy if exists "Anyone can read project comments" on public.project_comments;
create policy "Anyone can read project comments"
  on public.project_comments for select
  to anon, authenticated
  using (true);

drop policy if exists "Anyone can post valid project comments" on public.project_comments;
create policy "Anyone can post valid project comments"
  on public.project_comments for insert
  to anon, authenticated
  with check (
    char_length(btrim(name)) between 1 and 40
    and char_length(btrim(body)) between 1 and 500
  );

grant select, insert on table public.project_comments to anon, authenticated;
