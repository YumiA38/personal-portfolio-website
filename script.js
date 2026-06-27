const typedText = document.querySelector(".typed-text");

const roles = [
  "Junior Developer in Progress",
  "QA Tester in Progress",
  "IT Support Candidate",
  "Software Engineering Student"
];

let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeEffect() {
  if (!typedText) return;

  const currentRole = roles[roleIndex];

  if (isDeleting) {
    typedText.textContent = currentRole.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typedText.textContent = currentRole.substring(0, charIndex + 1);
    charIndex++;
  }

  let speed = isDeleting ? 45 : 80;

  if (!isDeleting && charIndex === currentRole.length) {
    speed = 1300;
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    roleIndex = (roleIndex + 1) % roles.length;
    speed = 350;
  }

  setTimeout(typeEffect, speed);
}

typeEffect();

const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", function () {
  let currentSection = "";

  sections.forEach(function (section) {
    const sectionTop = section.offsetTop - 140;

    if (window.scrollY >= sectionTop) {
      currentSection = section.getAttribute("id");
    }
  });

  navLinks.forEach(function (link) {
    link.classList.remove("active");

    if (link.getAttribute("href") === "#" + currentSection) {
      link.classList.add("active");
    }
  });
});

const copyEmailButton = document.querySelector("#copy-email");
const emailText = "yumiadem38@gmail.com";

if (copyEmailButton) {
  copyEmailButton.addEventListener("click", async function () {
    try {
      await navigator.clipboard.writeText(emailText);
      copyEmailButton.textContent = "Email copied!";
    } catch (error) {
      copyEmailButton.textContent = "Copy failed";
    }

    setTimeout(function () {
      copyEmailButton.textContent = "Copy Email";
    }, 2000);
  });
}

const year = document.querySelector("#year");

if (year) {
  year.textContent = new Date().getFullYear();
}
