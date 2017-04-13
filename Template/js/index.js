import InputGroup from "./input_group";


window.onload = () => {
	const inputGroups = InputGroup.initInputGroups();
	const generateButton = document.getElementById("generate-btn");
	generateButton.addEventListener("click", () => {
		generateVariant(InputGroup.getAllValues(inputGroups));
	});
};

function generateVariant(inputValues) {
	const queryParameters = inputValues.join(",");
	window.location.href = `get_temp_test/${queryParameters}`;
}