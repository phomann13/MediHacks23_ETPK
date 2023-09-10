const formToJSON = (elements) =>
  [].reduce.call(
    elements,
    (data, element) => {
        if(isValidElement(element) && isValidValue(element)){
        data[element.name] = element.value;
        }

      return data;
    },
    {}
  );

function handleSubmit(event) {
    event.preventDefault();

    const data = new FormData(event.target);

    const value =Object.fromEntries(data.entries());

    console.log({ value });
}

const handleFormSubmit = (event) => {
    event.preventDefault();

    const data = {};

    const dataContainer = document.getElementsByClassName('results__display')[0];

    dataContainer.textContent = JSON.stringify(data, null, ' ');
};

const form = document.getElementsByClassName('form')[0];
form.addEventListener('submit', handleFormSubmit);

const isValidElement = (element) => {
    return element.name && element.value;
};

const isValidValue = (element) => {
    return !['checkbox', 'radio'].includes(element.type) || element.checked;
};
