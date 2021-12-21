<template>
    <form class="area-form" @submit.prevent>
        <h3>Логин: </h3>
        <input class="input-area" type="text" name="username" id="username" placeholder="Логин" :value="username" @input="changeUsername">
        <h3>Пароль: </h3>
        <input class="input-area" type="password" name="password" id="password" placeholder="Пароль"  :value="password" @input="changePassword">
        <div class="area-button">
            <button class="button-style" @click="LogIn">Войти</button>
        </div>
    </form>
    
</template>

<script>
import axios from 'axios'
export default {
    name: 'SignInForm',
    data() {
        return {
            username: 'admin',
            password: 'admin',
        }
    },
    methods: {
        changeUsername(event) {
            this.username = event.target.value
        },
        changePassword(event) {
            this.password =event.target.value
        },
        async LogIn() {
            console.log('func LogIn');
            console.log(this.username);
            console.log(this.password);
            try {
                const response = await  axios.post(
                    'http://localhost:8000/api/auth/token/login/',
                    {
                        'username': this.username ,
                        'password': this.password,
                    },
                )
                if (response.status == 200) {
                    // Помещаем токен на хранение
                    localStorage.setItem('token', response.data.auth_token)
                    try {
                      const response = await axios.get('http://localhost:8000/api/users/me/', {
                        headers: {
                            'Authorization': 'token ' + (localStorage.getItem('token'))
                        }
                      })
                      console.log(response);
                      if (response.status == 200) {
                        localStorage.setItem('isComp', response.data.is_company)
                        this.$router.push({name: 'Home'})
                      }
                    } catch (error) {
                        console.error('Ошибка при просмотре профиля');
                    }
                }
                // TODO Сделать обработку ошибок
                
            } catch (error) {
                alert(error)
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
    width: 150px;
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