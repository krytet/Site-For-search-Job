<template>
    <form class="area-form" action="">
        <h3>Логин: </h3>
        <input class="input-area" type="text" name="username" id="username" placeholder="Логин">
        <h3>Пароль: </h3>
        <input class="input-area" type="password" name="password" id="password" placeholder="Пароль">
        <div class="area-button">
            <button class="button-style">Войти</button>
        </div>
    </form>
    
</template>

<script>
export default {
    name: 'SignInForm'

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
}
</style>