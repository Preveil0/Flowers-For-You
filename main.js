onload = () => {
  document.body.classList.remove("container");

  const openBtn = document.getElementById("openMessageBtn");
  const closeBtn = document.getElementById("closeLetterBtn");
  const overlay = document.getElementById("letterOverlay");
  const audio = document.getElementById("bg-music");
  const startOverlay = document.getElementById("start-overlay");

  const playAudio = () => {
      if (audio && audio.paused) {
          audio.volume = 0.75;
          audio.play().catch((err) => console.log("Audio play failed: ", err));
      }
  };

  // Handle start overlay
  if (startOverlay) {
      startOverlay.addEventListener("click", () => {
          startOverlay.classList.add("hidden");
          setTimeout(() => {
            startOverlay.style.display = 'none';
          }, 1000); // Wait for transition
          playAudio();
      });
  }

  // Fallback triggers just in case
  document.addEventListener("click", playAudio, { once: true });
  document.addEventListener("touchstart", playAudio, { once: true });

  if (openBtn && closeBtn && overlay) {
      openBtn.addEventListener("click", () => {
          overlay.style.display = "flex";
          playAudio();
      });

      closeBtn.addEventListener("click", () => {
          overlay.style.display = "none";
      });
  }
};
