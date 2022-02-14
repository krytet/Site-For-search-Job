<template>
    <form class="area-form" @submit.prevent>
        <h3>Название вакансии: </h3>
        <input class="input-area" type="text" name="name" id="name" placeholder="Название" v-model="name">
        <h3>Заробатная плата: </h3>
        <input class="input-area" type="number" name="salary" id="salary" placeholder="Заробатная плата" v-model="salary">
        
        <h3>Местоположение: </h3>
        <!-- TODO настроить под поиск-->
        <!-- TODO настроить под id-->
        <input class="input-area" type="text" name="location" id="location" placeholder="Местоположение" v-model="location" list="city">
        <datalist id="city">
            <option v-for="city in locationList" :key='city.id' :value="city.name"></option>
        </datalist>
        
        <!-- TODO настроить под id -->
        <h3>Спецальность: </h3>
        <input class="input-area" type="text" name="speciality" id="speciality" placeholder="Спецализация" v-model="speciality" list="specialitys">
        <datalist id="specialitys">
            <option v-for="specialit in specialityList" :key='specialit.id' :value="specialit.name">{{specialit.professional_area.name}}</option>
        </datalist>

        <!-- TODO сделть выподающий окно -->
        <h3>Навыки: </h3>
        <div>
            <div class="input-skills">
                <input class="input-area" type="text" name="skill" id="skill" placeholder="Навыки" v-model="skill">
                <button @click="AddSkill">Добавить</button>
            </div>
            <div class="elemets-skills">
                <div class="elemet-skills" v-for="skill in skills" :key="skill">
                    <span>{{ skill }}</span>
                    <button @click="DeleteSkill(skill)">
                        <img src="../image/delete.png" alt="delete">
                    </button>
                </div>
            </div>
        </div>
        

        <!-- TODO Проверить коректность работы -->
        <template v-for="radio in filters_elements.radio" :key="radio.value">
            <h3>{{ radio.name }}: </h3>
            <div>
                <template v-if="radio.value === 'experience'">
                    <RadioButton 
                        v-for="item in radio.items"
                        :item='item' 
                        :tag='radio.value' 
                        :key="item.value"
                        v-model:modelValue="experience"
                    />
                </template>

                <template v-else-if="radio.value === 'education'">
                    <RadioButton 
                        v-for="item in radio.items"
                        :item='item' 
                        :tag='radio.value' 
                        :key="item.value"
                        v-model:modelValue="education"
                    />
                </template>

                <template v-else-if="radio.value === 'type_employment'">
                    <RadioButton 
                        v-for="item in radio.items"
                        :item='item' 
                        :tag='radio.value' 
                        :key="item.value"
                        v-model:modelValue="type_employment"
                    />
                </template>

                <template v-else-if="radio.value === 'work_schedule'">
                    <RadioButton 
                        v-for="item in radio.items"
                        :item='item' 
                        :tag='radio.value' 
                        :key="item.value"
                        v-model:modelValue="work_schedule"
                    />
                </template>
            </div>
        </template>


        <h3>Возможность работать удаленно: </h3>
        <Switch 
            :element="data_remote"
            v-model:modelValue="remote_work"
        />

        <h3>Короткое описание: </h3>
        <textarea name="discriptionShort" id="discriptionShort" placeholder="Описание" v-model="discriptionShort" rows="5"></textarea>

        <h3>Описание: </h3>
        <textarea name="discription" id="discription" placeholder="Описание" v-model="discription" rows="10"></textarea>
        
        <div class="area-button">
            <button class="button-style" @click="CreateVacancy">Создать</button>
        </div>
    </form>
    
</template>

<script>
import axios from 'axios'
import Switch from '@/components/elements/Switch'
import RadioButton from '@/components/elements/RadioButton'


export default {
    name: 'SignUpForm',
    components: {
        Switch, RadioButton
    },
    data() {
        return {
            filters_elements: Object,
            isLoadingFilter: false,
            name: '',
            salary: null,
            locationList: [],
            location: '',
            specialityList: [],
            speciality: '',
            skill: '',
            skills: [],

            // TODO настроить ошибки 
            experience: 0,
            education: 0,
            type_employment: 0,
            work_schedule: 0,

            // TODO сделать автоматически 
            data_remote: {value: 'remote_work', name: ''},
            remote_work: false,
            discriptionShort: '',
            discription: '',
        }
    },
    methods: {
        async getFilterParams() {
            this.isLoadingFilter = true
            try {
                const response = await axios.get('http://localhost:8000/api/filter-params/')
                this.filters_elements = response.data
            } catch (error) {
                alert(error)
            }
            this.isLoadingFilter = false
        },

        async getLocations() {
            this.isLoadingFilter = true
            try {
                const response = await axios.get('http://localhost:8000/api/locations/')
                console.log('Locations');
                console.log(response);
                this.locationList = response.data
                console.log('elemessss');
                console.log(this.locationList);
                
            } catch (error) {
                alert(error)
            }
            this.isLoadingFilter = false
        },

        async getSpecialists() {
            this.isLoadingFilter = true
            try {
                const response = await axios.get('http://localhost:8000/api/specialists/')
                console.log('specialityList');
                console.log(response);
                this.specialityList = response.data
                console.log(this.specialityList);
                
            } catch (error) {
                alert(error)
            }
            this.isLoadingFilter = false
        },

        AddSkill() {
            if (this.skill != '') {
                this.skills.push(this.skill)
                this.skill = ''
            }
        },
        DeleteSkill(skill) {
            this.skills.splice(this.skills.indexOf(skill), 1)
        },

        async CreateVacancy() {
            console.log('func Vacancy');

            const vacancyData = {
                "name": this.name,
                "salary": this.salary,
                "location": this.location,
                "speciality": this.speciality,
                "skills": this.skills,
                "experience": this.experience,
                "education": this.education,
                "type_employment": this.type_employment,
                "work_schedule": this.work_schedule,
                "remote_work": this.remote_work,
                "short_discription": this.discriptionShort,
                "discription": this.discription,
            }
            console.log(vacancyData);
            
            try {
                const response = await axios.post(
                    // TODO изменить на страницу регистрации
                    'http://localhost:8000/api/vacancies/',
                    vacancyData,
                    {
                        headers: {
                            'Authorization': 'token ' + (localStorage.getItem('token'))
                        }
                    }
                )
                if (response.status == 200) {
                    // Помещаем токен на хранение
                    console.log('Создано')
                    // TODO сделать редерект
                }
                // TODO Сделать обработку ошибок
                
            } catch (error) {
                alert(error)
                console.error(error);
            }
        },
    },
    mounted() {
        this.getFilterParams();
        this.getLocations();
        this.getSpecialists();
    },

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

.input-skills button {
    width: 75px;
    height: 25px;
    border: 1px solid gray;
    margin-left: 10px;
    background-color: #8B5CF6;
    border-radius: 3px;
    justify-items: center;
    justify-content: center;
    justify-self: center;
    cursor: pointer;
    color: #000000;
    transition: 0.5s;
}

.input-skills button:hover {
    color: #4c00ff;
    transition: 0.5s;
}

.elemets-skills {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 300px;
    align-content: space-between;
}

.elemet-skills {
    background-color: rgb(202, 138, 218);
    display: flex;
    flex-direction: row;
    margin-right: 10px;
    margin-top: 10px;
    border-radius: 8px;
}

.elemet-skills span {
    align-self: center;
    margin-left: 5px;
}

.elemet-skills button {
    padding: 4px;
    border: none;
    background-color: #ffffff00;
    margin-left: 2px;
    padding-left: 2px;
    transition: 0.5s;
}

.elemet-skills button:hover {
    background-color: #ffffff30;
    transition: 0.5s;
}

.elemet-skills button img {
    width: 16px;
    height: 16px;
}



textarea {
    width: 200px;
    font-family: Arial, Helvetica, sans-serif;
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