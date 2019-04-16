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



function graficar() {
    var str_expr = document.getElementById("function_a").value;
    if (str_expr.length > 0){
        var quickplot = new QuickPlot(document.getElementById("canvas"));
        quickplot.setFunction(function (x) { return Math.pow(x, 2) });
        quickplot.setGraphDomain(-10, 10);
        quickplot.setGraphRange(-5, 5);
        quickplot.drawGraph();
    } else {
        alert("No se puede graficar por que la función esta vacia!")
    }
}
