<template>
    <div v-if="!isLoading" id="content-detail-jobs" class="content-detail-jobs">
        <DetailsVacancy :detail='detail' v-model:show="dialogVisible" />
        <DialogWindow v-model:show="dialogVisible">
            <h1> {{$route.params.id}} </h1>
            <FormSelectResume 
                v-model:show="dialogVisible" 
                v-model:select="selectResume" 
                :vacancy="$route.params.id"
            />
        </DialogWindow>
    </div>
    <LoadingSpiner v-else />
</template>

<script>
import DetailsVacancy from '@/components/DetailsVacancy'
import DialogWindow from '@/components/DialogWindow'
import FormSelectResume from '@/components/FormSelectResume'
import LoadingSpiner from '@/components/elements/LoadingSpiner'
import axios from 'axios'

export default {
    name: 'VacancyDetails',
    data() {
        return {
            dialogVisible: false,
            selectResume: 0,
            isLoading: true,
            detail: {}/**
                id_vacancy: 34,
                name_vacancy: 'Python разработчик (Django)',
                discription: '',
                skills: [
                    'Dango',
                    'Python',
                    'nginx',
                    'Postgres',
                    'Docker',
                    'Git',
                    'HTML',
                    'CSS',
                    'Dango',
                    'Python',
                    'nginx',
                    'Postgres',
                    'Docker',
                    'Git',
                    'HTML',
                ],
                salary: 123456,
                id_company: 2,
                name_company: 'HuskyJam',
                image: 'https://w7.pngwing.com/pngs/179/878/png-transparent-computer-icons-eagle-emblem-animals-logo.png',
                location: 'Москва',
                experience: 'От 6 лет',
                type_employment: 'Полная занятость',
                work_schedule: 'Полный день',
                education: 'Высшие',
                remote_work: true
            }*/
        }
    },
    components: {
        DetailsVacancy, DialogWindow, FormSelectResume, LoadingSpiner
    },
    methods: {
        async getVacancy() {
            this.isLoading = true
            try {
                console.log('метод');
                console.log(this.$route.params.id);
                const response = await axios.get(`http://localhost:8000/api/vacancies/${ this.$route.params.id }`)
                console.log(response.data);
                this.detail = response.data;
                console.log('!!!');
                console.log(this.detail);
            } catch(error) {
                alert(error)
                console.error('Ошибка');
                console.error(error)
            }
            this.isLoading = false
        }
    },
    mounted() {
        this.getVacancy()
        console.error('!!!!! Проверка');
        console.error(this.$route.params.id);
    }
}
</script>

<style scoped>
    .content-detail-jobs {
        display: grid;
        grid-template-areas: "left right";
        grid-column-gap: 30px;
        align-items: center;
        align-self:center;
        align-content: center;
        justify-self: center;
        justify-content: center;
        margin-bottom: 15px; 
        margin-top: 30px; 
    }

    h1 {
        background-color: rgb(219, 66, 66);
    }
</style>