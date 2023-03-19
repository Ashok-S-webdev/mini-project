var input = document.getElementById("dob");
var output = document.getElementById("age");

input.addEventListener("blur", () => {
	var dobString = input.value;
	var dob = new Date(dobString);
	var today = new Date();

	var month = today.getMonth() + 1;
	var bornMonth = dob.getMonth() + 1;

	var age = today.getFullYear() - dob.getFullYear();
	var monthDiff = month - bornMonth;

	if (isNaN(monthDiff)) {
		monthDiff = 0;
		output.value = age;
	}

	if (monthDiff > 0) {
		output.value = age;
	} else {
		output.value = age - 1;
	}
	console.log(monthDiff);
});
