onload = () => {
  document.body.classList.remove("container");

  const openBtn = document.getElementById("openMessageBtn");
  const closeBtn = document.getElementById("closeLetterBtn");
  const overlay = document.getElementById("letterOverlay");

  if (openBtn && closeBtn && overlay) {
      openBtn.addEventListener("click", () => {
          overlay.style.display = "flex";
      });

      closeBtn.addEventListener("click", () => {
          overlay.style.display = "none";
      });
  }
};
