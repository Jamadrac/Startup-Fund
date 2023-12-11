function reveal() {
    var reveals = document.querySelectorAll(".reveal");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  
  window.addEventListener("scroll", reveal);

// fading effect
  const textArray = [
    "For Statups Owners",
    "Sign Up/Sign In", 
    "Register your startup",
    "Connect with Investers",
    "For Investers",
    "Sign up/Sign In",
    "Find a startup",
    "Study it and analyse",
    "Buy shares/Acquire it"
    // Add more phrases as needed
  ];

  let currentIndex = 0;
  const changingText = document.getElementById("changing-text");

  function changeText() {
    changingText.textContent = textArray[currentIndex];
    currentIndex = (currentIndex + 1) % textArray.length;
  }

  setInterval(changeText, 4000);

// dropdown
function toggleDropdown() {
  const dropdown = document.querySelector('.dropdown');
  dropdown.classList.toggle('active');
}