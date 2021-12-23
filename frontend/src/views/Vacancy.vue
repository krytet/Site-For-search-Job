<template>
    <LoadingSpiner v-if="isLoadingFilter && isLoadingVacancy"/>
    <div class="content">
        <Filter v-model="filtersParams" :filters_elements='filters_elements' @change="ChangeFilter" />
        <ListVacancy v-model="selectedSort" :vacancies='vacancies' />
        <RightTopCompany :top_companies="top_companies" />
        

    </div>
</template>

<script>
import Filter from '@/components/Filter'
import ListVacancy from '@/components/ListVacancy'
import RightTopCompany from '@/components/RightTopCompany'
import LoadingSpiner from '@/components/elements/LoadingSpiner'
import axios from "axios"
import { vacancyListApi } from '@/api/index'

export default {
    name: 'VacancyList',
    data() {
        return {
            isLoadingFilter: false,
            isLoadingVacancy: false,
            selectedSort: null,
            filtersParams: {
                experience: null,
                type_employment: null,
                work_schedule: null,
                education: null,
                remote_work: null,
                disability: null,
            },
            filters_elements: {}, /**
                radio :{
                    experience: {
                        value: 'experience',
                        name: 'Опыт работы',
                        items: [
                            {
                                id: 1,
                                name: 'Нет опыта'
                            },
                            {
                                id: 2,
                                name: 'От 1 до 3 лет'
                            },
                            {
                                id: 3,
                                name: 'От 3 лет'
                            },
                        ]
                    },
                    type_employment: {
                        value: 'type_employment',
                        name: 'Тип занятости',
                        items: [
                            {
                                id: 1,
                                name: 'Полная'
                            },
                            {
                                id: 2,
                                name: 'Частичная'
                            },
                            {
                                id: 3,
                                name: 'Стажировка'
                            },
                        ]
                    },
                    work_schedule: {
                        value: 'work_schedule',
                        name: 'График работы',
                        items: [
                            {
                                id: 1,
                                name: 'Полный'
                            },
                            {
                                id: 2,
                                name: 'Гибкий'
                            },
                            {
                                id: 3,
                                name: 'Свободный'
                            },
                        ]
                    },
                    education: {
                        value: 'education',
                        name: 'Образование',
                        items: [
                            {
                                id: 1,
                                name: 'Среднее'
                            },
                            {
                                id: 2,
                                name: 'Неполное высшие'
                            },
                            {
                                id: 3,
                                name: 'Высшие'
                            },
                        ]
                    },
                },
                switch_elements: {
                    remote_work: {
                        value: 'remote_work',
                        name: 'Удаленная работа',
                    },
                }
            }, */
            vacancies: [], /**
                {
                    id: 23,
                    image: '@/image/Avatar.png',
                    name_company: 'AgencyAnalytics...',
                    city: 'Almaty..',
                    data_age: 0,
                    name_job: 'Frontend Developer (Website)...',
                    discription: 'Our remote company is seeking a passionate .' +
                        'person to become the lead developer on our websit..e.',
                    is_like: true,
                },
                {
                    id: 22,
                    image: '@/image/Avatar.png',
                    name_company: 'AgencyAnalytics',
                    city: 'Kiev',
                    data_age: 0,
                    name_job: 'Frontend Developer (Website)',
                    discription: 'Our remote company is seeking a passionate ' +
                        'person to become the lead developer on our website.',
                    is_like: false,
                },
                {
                    id: 21,
                    image: '@/image/Avatar.png',
                    name_company: 'AgencyAnalytics',
                    city: 'Kiev',
                    data_age: 5,
                    name_job: 'Frontend Developer (Website)',
                    discription: 'Our remote company is seeking a passionate ' +
                        'person to become the lead developer on our website.',
                    is_like: false,
                },
            ], */
            top_companies: [
                {
                    id: 23,
                    name: 'AgencyAnalytics',
                    src: 'https://w7.pngwing.com/pngs/946/514/png-transparent-logo-logo-template-grey-logo-for-free-logo-element-line-thumbnail.png',
                },
                {
                    id: 25,
                    name: 'Sony PlayStaition',
                    src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Playstation_logo_colour.svg/350px-Playstation_logo_colour.svg.png',
                },
                {
                    id: 47,
                    name: 'AgencyAnalytics',
                    src: 'https://i0.pngocean.com/files/212/540/940/logo-banner-health-care-home-care-service-logo-design-thumb.jpg',
                },
            ],
        }
    },
    components: {
        Filter,
        ListVacancy,
        RightTopCompany,
        LoadingSpiner,
    },
    methods: {
        async getPost () {
            try {
                const response = await axios.get('https://jsonplaceholder.typicode.com/posts')
                console.log(response);
            } catch(e) {
                console.error(e);
            }
        },
        async getFilterParams() {
            this.isLoadingFilter = true
            try {
                const response = await axios.get('http://localhost:8000/api/filter-params/')
                console.log('Filter Params');
                console.log(response);
                this.filters_elements = response.data
            } catch (error) {
                alert(error)
            }
            this.isLoadingFilter = false
        },
        async getVacancy(
            experience = null,
            type_employment = null,
            work_schedule = null,
            education = null,
            remote_work = null,
            sort = null
        ) {
            this.isLoadingVacancy = true
            try{
                const response = await axios.get('http://localhost:8000/api/vacancies/', {
                    params: {
                        format: 'json',
                        experience: experience,
                        type_employment: type_employment,
                        work_schedule: work_schedule,
                        education: education,
                        remote_work: remote_work,
                        sort: sort
                    }
                });
                console.log('Vacancy')
                console.log(response)
                console.log(response.data)
                console.log(response.data.results)
                
                this.vacancies = response.data.results
            } catch(error) {
                alert(error)
                console.error('Ошибка');
                console.error(error)
            }
            this.isLoadingVacancy = true
        },
        ChangeFilter(event) {
            this.getVacancy(
                this.filtersParams.experience,
                this.filtersParams.type_employment,
                this.filtersParams.work_schedule,
                this.filtersParams.education,
                this.filtersParams.remote_work,
                this.selectedSort,
            ) 
        }
    },
    mounted() {
        this.getVacancy(
            this.filtersParams.experience,
            this.filtersParams.type_employment,
            this.filtersParams.work_schedule,
            this.filtersParams.education,
            this.filtersParams.remote_work,
            this.selectedSort,
        )
        this.getFilterParams()
    },
    watch: {
        selectedSort(newParams) {
            console.log('whatch')
            console.log(newParams)
            this.getVacancy(
                this.filtersParams.experience,
                this.filtersParams.type_employment,
                this.filtersParams.work_schedule,
                this.filtersParams.education,
                this.filtersParams.remote_work,
                this.selectedSort,
            ) 
            console.log(newParams)
        }
    }
}
</script>

<style scoped>
    .content{
        display: grid;
        grid-template-columns: 200px 700px 256px ;
        grid-column-gap: 3%;
        padding-top: 32px;
        justify-content: center;
        justify-self:center;
    }
</style>