const usernameField=document.querySelector('#usernameField');
const usersurnameField=document.querySelector('#usersurnameField')
const feedBackArea = document.querySelector(".invalid_feedback");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const usersurnameSuccessOutput = document.querySelector(".usersurnameSuccessOutput");
const submitBtn = document.querySelector(".submit-btn");
const emailField = document.querySelector("#emailField");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const passwordField = document.querySelector("#passwordField");
const showPasswordToggle = document.querySelector(".showPasswordToggle");

const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === "Показать") {
    showPasswordToggle.textContent = "Скрыть";
    passwordField.setAttribute("type", "text");
  } else {
    showPasswordToggle.textContent = "Показать";
    passwordField.setAttribute("type", "password");
  }
};

showPasswordToggle.addEventListener("click", handleToggleInput);


//имя
usernameField.addEventListener("keyup", (e) => {
   const usernameVal = e.target.value;

    usernameSuccessOutput.style.display = "block";

  usernameSuccessOutput.textContent = `Checking  ${usernameVal}`;

   usernameField.classList.remove("is-invalid");
   feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
         usernameSuccessOutput.style.display = "none";
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

//фамилия
usersurnameField.addEventListener("keyup", (e) => {
   const usersurnameVal = e.target.value;

    usersurnameSuccessOutput.style.display = "block";

  usersurnameSuccessOutput.textContent = `Checking  ${usersurnameVal}`;

   usersurnameField.classList.remove("is-invalid");
   feedBackArea.style.display = "none";

  if (usersurnameVal.length > 0) {
    fetch("/authentication/validate-usersurname", {
      body: JSON.stringify({ usersurname: usersurnameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
         usersurnameSuccessOutput.style.display = "none";
        if (data.usersurname_error) {
          usersurnameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.usersurname_error}</p>`;
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});



emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;

  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/authentication/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.email_error) {
          submitBtn.disabled = true;
          emailField.classList.add("is-invalid");
          emailFeedBackArea.style.display = "block";
          emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});