let currentOperation = "";
let storedNumber = null;
let currentOperator = null;
let currentOperatorButton = null;

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
            display.value = "";
            currentOperation = "";
            storedNumber = null;
            currentOperator = null;

            if (currentOperatorButton) {
                currentOperatorButton.classList.remove('active');
                currentOperatorButton = null;
            }
        } else if (clearBtn.value === "C") {
            display.value = display.value.slice(0,-1);
        }

        updateClearButton();
    }

    function updateClearButton() {
        let display = document.getElementById('display');
        let clearBtn = document.getElementById('clearBtn');

        if (display.value === "") {
            clearBtn.value = "AC";
        } else {
            clearBtn.value = "C";
        }
    }

    function handleNumberInput(value) {
        let display = document.getElementById('display');
        let currentValue = display.value;

        if (currentOperator === null && storedNumber !== null) {
            display.value = '';
        }
        display.value += value;
    }

    function handleOperator(operator, button) {
        let display = document.getElementById('display');
    
        if (currentOperator) {
            calculateResult();
        }
    
        
        storedNumber = parseFloat(display.value) || storedNumber;
        currentOperator = operator;
        display.value = '';
    
        if (currentOperatorButton) {
            currentOperatorButton.classList.remove('active');
        }
        button.classList.add('active');
        currentOperatorButton = button;
    }

    function calculateResult() {
        let display = document.getElementById('display');
        let currentValue = parseFloat(display.value);
        
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
            storedNumber = null;
            currentOperator = null;

            if (currentOperatorButton) {
                currentOperatorButton.classList.remove('active');
                currentOperatorButton = null;
            }
        }
    }
    
    window.onload = updateClearButton;

    document.getElementById('display').addEventListener('input', updateClearButton);