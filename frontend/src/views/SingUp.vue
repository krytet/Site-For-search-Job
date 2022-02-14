<template>
    <div class="signup">
        <div class="login-area">
        <h1>Регистрация</h1>

        <div class="select-type-user">
            <BigRadioButton 
                v-for="item in typeUser"
                v-model:modelValue="isCreateComp"
                :item='item' 
                :tag='tag'
                :key="item.id"
                @change="ChangeRadio"
            />
        </div>
        
        <SignUpForm 
            v-if="isCreateComp != Boolean"
            :isCreateComp='isCreateComp' 
        />

        </div>
    </div>
</template>

<script>
import SignUpForm from '@/components/SignUpForm'
import BigRadioButton from '@/components/elements/BigRadioButton'

export default {
    name: 'SingUp',
    data() {
        return {
            isCreateComp: Boolean,
            tag: 'typeUser',
            typeUser: [
                {
                    id: 1,
                    name: "Я ищу работу",
                    isComp: false
                },
                {
                    id: 2,
                    name: "Я ищу сотрудников",
                    isComp: true
                },
            ]
        }
    },
    components: {
        SignUpForm, BigRadioButton
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