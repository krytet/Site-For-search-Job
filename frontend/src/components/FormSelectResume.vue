<template>
    <div class="form-bg">
        <h1>Выберите резюме</h1>
        <form class="form-area" @submit.prevent>
            <h3>Список</h3>
            <!--CardResume v-model:select="select" :resumeDetail='resume' /-->
            <div>
                <RadioButton v-for="resume in resumies" :key="resume.id" :item="resume" :tag='"resum"' v-model="select" />
            </div>
            <button class="response-vacancy" @click="ResponseVacanse">Откликнуться</button>
        </form>
    </div>
</template>

<script>
import CardResume from '@/components/CardResume'
import RadioButton from '@/components/elements/RadioButton'
import axios from 'axios'
export default {
    name: 'FormSelectResume',
    data() {
        return {
            select: 0,
            resumies: [
                {
                    id: 43,
                    name: 'Разработчик'
                },
                {
                    id: 433,
                    name: 'Програмист'
                },
                {
                    id: 443,
                    name: 'Backend'
                },
            ]
        }
    },
    components: {
        CardResume, RadioButton
    },
    props: {
        show: {
            type: Boolean
        }
    },
    methods: {
        async ResponseVacanse(event) {
            console.log('click');
            try {
                const response = await axios.post(
                    `http://localhost:8000/api/vacancies/${this.$route.params.id}/response/`,
                    {
                        'resume': this.select
                    },
                    {
                        headers: {
                            'Authorization': 'token ' + (localStorage.getItem('token'))
                        }
                    }
                )
                if (response.status == 201) {
                    this.$emit('update:show', false)
                } else {
                    console.error('Статус не 200');
                }
            } catch (error) {
                alert(error)
            }
        },
        async getMyResume() {
            console.log('Get My Resume');
            try {
                const response = await axios.get(
                    'http://localhost:8000/api/resumes/my/',
                    {
                        headers: {
                            'Authorization': 'token ' + (localStorage.getItem('token'))
                        }
                    }
                )
                console.log(response);
                console.log(response.data);
                this.resumies = response.data
            } catch (error) {
                alert(error)
            }
        }
    },
    mounted() {
        this.getMyResume()
    }
}
</script>

<style scoped>
.form-bg {
    background-color: #F3F4F6;
    padding: 30px;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
}

.form-area {
    display: flex;
    flex-direction: column;
}

.response-vacancy {
    background-color: rgb(202, 138, 218);
    font-size: 16px;
    border: 1px solid #E4E4E7;
    border-radius: 5px;
    text-decoration: none;
    padding: 10px;
    color: black;
    margin: 10px;
    align-self: center;
}
</style>