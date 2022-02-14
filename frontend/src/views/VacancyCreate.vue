<template>
    <div class="signup">
        <div class="login-area">
        <h1>Создание вакансии</h1>

        <FormCreateVacancy />

        </div>
    </div>
</template>

<script>
import FormCreateVacancy from '@/components/FormCreateVacancy'

export default {
    name: 'SingUp',
    data() {
        return {
        }
    },
    components: {
        FormCreateVacancy
    },
}
</script>

<style scoped>
.signup {
    display: flex;
    background-color: rgba(255, 255, 255, 0.329);
    border-radius: 50px;
    max-width: 1000px;
    border: 2px solid rgb(94, 85, 85);
    margin: 20px auto;
    min-height: 400px;
    align-items: center;
}

.select-type-user  {
    display: flex;
}

.select-type-user  label{
    margin: 5px 15px;
}

.login-area {
    margin: 10px auto;
    width:max-content;
    display: flex;
    flex-direction: column;
    align-items: center;
}

</style>