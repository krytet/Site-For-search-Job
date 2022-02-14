<template>
    <form class="area-form" @submit.prevent>
        <h3>Логин: </h3>
        <input class="input-area" type="text" name="username" id="username" placeholder="Логин" v-model="username">
        <h3>E-mail: </h3>
        <input class="input-area" type="email" name="email" id="email" placeholder="Адрес электронной почты" v-model="email">
        
        <template v-if="isCreateComp == `true`">
            <h3>Полноеназвание компании: </h3>
            <input class="input-area" type="text" name="first_name" id="first_name" placeholder="Полное название компании" v-model="first_name">
            <h3>Короткое название компании: </h3>
            <input class="input-area" type="text" name="last_name" id="last_name" placeholder="Название компании" v-model="last_name">
        </template>

        <template v-else>
            <h3>Имя: </h3>
            <input class="input-area" type="text" name="first_name" id="first_name" placeholder="Имя" v-model="first_name">
            <h3>Фамилия: </h3>
            <input class="input-area" type="text" name="last_name" id="last_name" placeholder="Фамилия" v-model="last_name">
            <h3>Отчество: </h3>
            <input class="input-area" type="text" name="patronymic" id="patronymic" placeholder="Отчество" v-model="patronymic">
        </template>
        
        <h3>Номер телефона: </h3>
        <input class="input-area" type="tel" name="number" id="number" placeholder="Номер телефона" v-model="number">
        <h3>Пароль: </h3>
        <input class="input-area" type="password" name="password" id="password" placeholder="Пароль"  v-model="password">
        <div class="area-button">
            <button class="button-style" @click="SignUp">Регистрация</button>
        </div>
    </form>
    
</template>

<script>
import axios from 'axios'
export default {
    name: 'SignUpForm',
    props: {
        isCreateComp: {
            type: Boolean
        }
    },
    data() {
        return {
            username: 'admin',
            password: 'admin',
            first_name: '',
            last_name: '',
            patronymic: '',
            email: '',
            number: '',
        }
    },
    methods: {
        async SignUp() {
            console.log('func SignUp');
            console.log(this.username);
            console.log(this.password);
            const registerData = {
                'username': this.username ,
                'password': this.password,
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'number': this.number,
                'is_company': this.isCreateComp
            }
            if (this.patronymic) {
                registerData['patronymic'] = this.patronymic
            }
            
            try {
                const response = await  axios.post(
                    // TODO изменить на страницу регистрации
                    'http://localhost:8000/api/users/',
                    registerData,
                );
                console.log(response);
                if (response.status == 200) {
                    // Помещаем токен на хранение
                    console.log('Создано')
                    // TODO сделать редерект
                }
                // TODO Сделать обработку ошибок
                
            } catch (error) {
                alert(error);
                console.error(error);
            }
        },
    }

}
</script>

<style scoped>
.area-form {
    max-width: max-content;
    display: grid;
    grid-template-columns: auto auto;
    grid-gap: 15px;
    align-items: center;
}

.area-form h3 {
    cursor: default;
}

.input-area {
    height: 25px;
    text-align: center;
    width: 200px;
    vertical-align: middle;
}

.area-button {
    grid-column-start: 1;
    grid-column-end: 3;
    display: flex;
    justify-content: center;
}

.button-style {
    width: 100px;
    height: 30px;
    border: 1px solid gray;
    background-color: #8B5CF6;
    border-radius: 3px;
    justify-items: center;
    justify-content: center;
    justify-self: center;
    cursor: pointer;
}
</style>