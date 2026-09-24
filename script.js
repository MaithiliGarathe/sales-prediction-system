function predictSales() {

    // Get values entered by the user
    const tv = parseFloat(document.getElementById("tv").value);
    const radio = parseFloat(document.getElementById("radio").value);
    const newspaper = parseFloat(document.getElementById("newspaper").value);

    // Check whether all values are entered
    if (isNaN(tv) || isNaN(radio) || isNaN(newspaper)) {
        document.getElementById("prediction").innerText =
            "Please enter all values";
        return;
    }

    // Linear Regression prediction
    const prediction =
        MODEL.intercept +
        MODEL.tv * tv +
        MODEL.radio * radio +
        MODEL.newspaper * newspaper;

    // Display prediction
    document.getElementById("prediction").innerText =
        prediction.toFixed(2) + " thousand units";

    // Display the calculation
    document.querySelector(".result-card p").innerText =
        "Prediction calculated using the trained Linear Regression model.";
}