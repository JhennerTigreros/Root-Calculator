function OnSelectionChange(select) {
    var selectedOption = parseInt(select.options[select.selectedIndex].value);
    console.log(selectedOption)

    if (selectedOption == 1) {
        document.numericMethods.action = "/calculate/root/bisection";
    } else if (selectedOption == 2) {
        document.numericMethods.action = "/calculate/root/fake-position";
    } else if (selectedOption == 3) {
        document.numericMethods.action = "/calculate/root/fake-position-mod";
    } else if (selectedOption == 4) {
        document.numericMethods.action = "/calculate/root/newton-raphson";
    } else if (selectedOption == 5) {
        document.numericMethods.action = "/calculate/root/sec";
    }
}