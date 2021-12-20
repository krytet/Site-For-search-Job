<template>
    <div class="signin">
        <div class="login-area">
        <h1>Авторизация</h1>
        <SignInForm />

        </div>
    </div>
</template>

<script>
import SignInForm from '@/components/SignInForm'

export default {
    name: 'SingIn',
    components: {
        SignInForm
    },
}
</script>

<style scoped>
.signin {
    display: flex;
    background-color: rgba(255, 255, 255, 0.329);
    border-radius: 50px;
    max-width: 1000px;
    border: 2px solid rgb(94, 85, 85);
    margin: 20px auto;
    min-height: 400px;
    align-items: center;

}

.login-area {
    margin: 10px auto;
    width:max-content;
    display: flex;
    flex-direction: column;
    align-items: center;
}

</style>