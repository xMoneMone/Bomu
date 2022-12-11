const profilePicInput = document.getElementById("id_profile_pic");
const profilePic = document.getElementById("profile-picture-image");

profilePicInput.onchange = evt => {
    const [file] = profilePicInput.files
    if (file) {
      profilePic.src = URL.createObjectURL(file)
    }
  }
