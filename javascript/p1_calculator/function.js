let currentOperation = "";
let storedNumber = null;
let currentOperator = null;
let currentOperatorButton = null;
let readyForNewInput = false;

    function toggleSign() {
        let currentValue = document.getElementById('display').value;
        if(currentValue) {
            if (currentValue.charAt(0) === '-'){
                document.getElementById('display').value = currentValue.slice(1);
            } else {
                document.getElementById('display').value = '-' + currentValue;
            }
        }
    }

    function calculatePercentage() {
        let currentValue = document.getElementById('display').value;
        if(currentValue) {
                document.getElementById('display').value = parseFloat(currentValue) / 100;
            }
    }

    function handleClear() {
        let display = document.getElementById('display');
        let clearBtn = document.getElementById('clearBtn');

        if (clearBtn.value === "AC") {
            display.value = "0";
            currentOperation = "";
            storedNumber = null;
            currentOperator = null;
            readyForNewInput = false;

            if (currentOperatorButton) {
                currentOperatorButton.classList.remove('active');
                currentOperatorButton = null;
            }
        } 
        updateClearButton();
    }

    function updateClearButton() {
        let display = document.getElementById('display');
        let clearBtn = document.getElementById('clearBtn');

        if (display.value === "0" || display.value === "") {
            clearBtn.value = "AC";
        } 
    }

    function handleNumberInput(value) {
        let display = document.getElementById('display');

        if (readyForNewInput || display.value === "0") {
            display.value = value;
            readyForNewInput = false;
        } else {
            display.value += value;
        }
    }


    function handleOperator(operator, button) {
        let display = document.getElementById('display');
    
        if (currentOperator) {
            calculateResult();
        }
    
        
        storedNumber = parseFloat(display.value) || storedNumber;
        currentOperator = operator;
        readyForNewInput = true;
    
        if (currentOperatorButton) {
            currentOperatorButton.classList.remove('active');
        }
        button.classList.add('active');
        currentOperatorButton = button;
    }

    function calculateResult() {
        let display = document.getElementById('display');
        let currentValue = parseFloat(display.value);

        if (!currentValue && storedNumber !== null) {
            currentValue = storedNumber;
        }
        
        if (storedNumber !== null && currentOperator) {
            let result;
            switch (currentOperator) {
                case '+':
                    result = storedNumber + currentValue;
                    break;
                case '-':
                    result = storedNumber - currentValue;
                    break;
                case '*':
                    result = storedNumber * currentValue;
                    break;
                case '/':
                    result = storedNumber / currentValue;
                    break;
                default:
                    result = currentValue;
            }
        
            display.value = result;
            readyForNewInput = true;

            storedNumber = null;
            currentOperator = null;

            if (currentOperatorButton) {
                currentOperatorButton.classList.remove('active');
                currentOperatorButton = null;
            }
        }
    }
    
    window.onload = function() {
        let display = document.getElementById('display');
        display.value = '0';
        updateClearButton();
    };

        document.getElementById('display').addEventListener('input', updateClearButton);

        