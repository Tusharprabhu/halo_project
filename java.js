let input = document.getElementById('result');

function appendCharacter(character) {
  input.value += character;
}

function appendFunction(func) {
  input.value += `${func}(`;
}

function calculate() {
  try {
    let result = eval(input.value);
    input.value = result;
  } catch (error) {
    input.value = 'Error';
  }
}

function clearInput() {
  input.value = '';
}

function deleteLast() {
  input.value = input.value.slice(0, -1);
}
