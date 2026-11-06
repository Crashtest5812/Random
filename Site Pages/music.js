const musicToggle = document.querySelector("[data-site-music-toggle]");
const musicStatus = document.querySelector("[data-site-music-status]");
const musicTrack = document.body.dataset.musicTrack;
const musicPreferenceKey = "random-projects-music-enabled";

if (musicToggle && musicTrack) {
  const music = new Audio(musicTrack);
  music.loop = true;
  music.volume = 0.2;
  music.preload = "none";

  let musicEnabled = false;
  let storageAvailable = true;

  try {
    musicEnabled = localStorage.getItem(musicPreferenceKey) === "true";
  } catch (error) {
    storageAvailable = false;
    console.error("Could not read the music preference.", error);
    musicStatus.textContent = "Music preference storage is unavailable; music is off.";
  }

  function updateMusicButton() {
    musicToggle.setAttribute("aria-pressed", String(musicEnabled));
    musicToggle.textContent = `Music: ${musicEnabled ? "on" : "off"}`;
  }

  function saveMusicPreference() {
    if (!storageAvailable) return;
    try {
      localStorage.setItem(musicPreferenceKey, String(musicEnabled));
    } catch (error) {
      storageAvailable = false;
      console.error("Could not save the music preference.", error);
      musicStatus.textContent = "Could not save your music choice; it may reset when you leave.";
    }
  }

  async function startMusic() {
    try {
      await music.play();
      if (storageAvailable) musicStatus.textContent = "";
    } catch (error) {
      console.warn("Background music could not start.", error);
      musicStatus.textContent = "Music is on. Press the music button again to start playback.";
    }
  }

  updateMusicButton();
  musicToggle.addEventListener("click", () => {
    if (musicEnabled && music.paused) {
      startMusic();
      return;
    }

    musicEnabled = !musicEnabled;
    updateMusicButton();
    saveMusicPreference();

    if (musicEnabled) {
      startMusic();
    } else {
      music.pause();
      music.currentTime = 0;
      musicStatus.textContent = storageAvailable ? "" : "Music is off. Your choice could not be saved.";
    }
  });

  if (musicEnabled) startMusic();
}
