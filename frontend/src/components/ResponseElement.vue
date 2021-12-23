<template>
    <div v-if="isExist" class="card-response">
        <div class="status-and-resume">
            <h3 v-if="response.status.id <= 2" style="color: #71717A"> {{response.status.name}}</h3>
            <h3 v-if="response.status.id == 3" style="color: green"> {{response.status.name}}</h3>
            <h3 v-if="response.status.id == 4" style="color: red"> {{response.status.name}}</h3>
            <h3 v-if="response.status.id == 5" style="color: blue"> {{response.status.name}}</h3>
            <div v-if="response.status.id == 1">
                <button @click="setVisibilyteResume(response.id, response.resume.id, response.vacancy.id)">
                    <img src="@/image/edit.png" alt="edit">
                </button>
                <button @click="deleteRespose(response.id)">
                    <img src="@/image/delete.png" alt="delete">
                </button>
            </div>
        </div>
        <div class="vacancy-and-company">
            <router-link :to="{ path: '/vacancy/' + response.vacancy.id }" style="text-decoration: none; color: inherit;">
                <h3> {{ response.vacancy.name }} </h3> 
            </router-link>
            <router-link :to="{ path: '/companies/' + response.vacancy.author.id }" style="text-decoration: none; color: inherit;">
                <h4> {{response.vacancy.author.first_name}} </h4> 
            </router-link>
        </div>
        <div class="data">
            <span>Сегодня</span>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'ResponseElement',
    data() {
        return {
            isExist: true
        }
    },
    props: {
        watchResponse: {
            type: Number
        },
        watchResponseSelect: {
            type: Number
        },
        watchResponseVacancy: {
            type: Number
        },
        showResume: {
            type: Boolean
        },
        response: {
            type: Object,
            requred: true
        }
    },
    methods: {
        setVisibilyteResume(idResponse, idResume, idVacancy) {
            console.log('Тал видемым');
            this.$emit('update:showResume', true)
            this.$emit('update:watchResponse', idResponse)
            this.$emit('update:watchResponseSelect', idResume)
            this.$emit('update:watchResponseVacancy', idVacancy)
        },
        async deleteRespose(idResponse) {
            console.log(idResponse)
            try {
                const response = await axios.delete(
                    `http://localhost:8000/api/responses/${idResponse}/`,
                    {
                        headers: {
                            'Authorization': 'token ' + (localStorage.getItem('token'))
                        }
                    }
                )
                this.isExist = false
            } catch (error) {
                alert(error)
            }
        }
    }
}
</script>

<style scoped>
.card-response {
    display: grid;
    grid-template-columns: 300px auto 100px;
    border-radius: 5px;
    padding: 5px;
    transition: 0.5s;
}

.card-response:hover {
    background-color: #F3F4F6;
    transition: 0.5s;
    padding: 6px;
}

button {
    background: none;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    margin-left: 15px;
    transition: 0.5s;
}

button:hover {
    background: #fff;
    transition: 0.2s;
}

img {
    height: 16px;
    width: 16px;
    margin: 5px;
}

.vacancy-and-company h4 {
    color: #71717A;
}

</style>