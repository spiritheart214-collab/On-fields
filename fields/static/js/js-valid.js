// JUST VALIDATE ---------------------------
// Форма обратной связи
new JustValidate (".js-form-connection", {
    rules:{
  
      name:{
        required: true,
        minLength: 2,
        maxLength: 30,
      },
  
      textarea: {
        required: true,
        minLength: 10,
        maxLength: 300,
      },
    },
  
    messages: {
      name: {
        required: 'Поле обязательно к заполнению ',
        minLength:'Необходимо ввести имя целиком',
        maxLength: 'Необходимо ввести только имя',
      },
  
      textarea: {
        required: "Поле обязательно к заполнению",
        minLength: "Сообщение должно содержать не менее 10 символов",
        maxLength: "Сообщение должно содержать не более 300 символов",
      },
    },
  
    tooltip: {
      fadeOutTime: 4000,
    },
    colorWrong: 'red',

});