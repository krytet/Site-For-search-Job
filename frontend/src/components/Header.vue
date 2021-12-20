<template>
    <header>
            <div id="top" class="top">
                <div>
                    <router-link to="/"><img src="@/image/logo.png" alt="logo"></router-link>
                </div>
                <input type="text" name="search" id="input_search" placeholder="Find your best job">
                <div id="menu" class="menu">
                    <router-link to="/">
                        <button class="menu-button">
                            Чаты
                        </button>
                    </router-link>
                    <router-link to="/">
                        <button class="menu-button">
                            Отклики
                        </button>
                    </router-link>
                    <button class="menu-button" @click="SignOut">
                        Выйти
                    </button>
                </div>
                <button>Создать резюме</button>
            </div>
            <div id="logo" class="logo">
                <div id="slogan" class="slogan">
                    <h1>Top jobs board for professionals</h1>
                    <h5>Discover your next career move with over 15 000 opening 
                        vacancies, customer support, sowtware, design anywhere in 
                        the world or remotely.
                    </h5>
                </div>
            </div>
        </header>
</template>

<script>
import logo from '@/image/logo.png'
import background from '@/image/background.png'
import axios from 'axios';

export default {
    name: 'Header',
    components:{
        logo
    },
    methods: {
        async SignOut() {
            try {
                const response = await axios.post(
                    'http://localhost:8000/api/auth/token/logout/',
                    {}, 
                    {
                        headers: {
                            'Authorization': 'token ' + (localStorage.getItem('token'))
                        }
                    }
                )
                if (response.status == 204) {
                    localStorage.removeItem('token')
                    localStorage.removeItem('isComp')
                }
            } catch (error) {
                alert(error)
                console.error(error);
            }
        },
    }
}
</script>

<style scoped>
    #header{
        display: flex;
        flex-direction: column;
    }

    .top{
        display: flex;
        flex-direction: row;
        height: 37px;
        padding: 17.5px 100px;
        align-items: center;
    }

    .top input {
        flex-grow: 1;
        background: none;
        border: none;
        margin-left: 15px;
    }

    .top input::placeholder{
        color: #A1A1AA;
    }

    .top a {
        color: #71717A;
        text-decoration: none;
        font-size: 14px;
        font-family: 'Helvetica', 'Neue';
        margin-left: 25px;
    }

    

    .top button{
        background-color: #7C3AED;
        color: #F3F4F6;
        border: none;
        border-radius: 3px;
        height: 37px;
        width: 98px;
        padding: 0;
        margin-left: 27.5px;
    }

    button.menu-button {
        color: #71717A;
        background-color:rgba(255, 255, 255, 0);
        font-size: 14px;
        font-family: 'Helvetica', 'Neue';
        text-decoration: none;
        cursor: pointer;
        width: min-content;
    }

    #input:focus{
        outline: none;
    }

    #h5 {
        margin: 0px;
    }
    .logo {
        background-image: url("~@/image/background.png");
        background-size: cover;
        display: flex;
        flex-direction: column;
        text-align: center;
        height: 330px;
    }

    .slogan {
        margin: auto;
        color: #FFFFFF;
    }

    .slogan h1 {
        font-size: 48px;
        max-width: 584px;
    }

    .slogan h5 {
        max-width: 410px;
        font-size: 16px;
        margin: auto;
    }

</style>