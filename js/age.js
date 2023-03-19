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

	if (bornMonth < month) {
		age -= 1;
	} else {
		//pass
	}
	output.value = age;
});
