<template>
    <div class="area-reponses">
        <h1>Список откликов</h1>
        <div>
            <span> Когда нибудь здесь будет сортировка, но опка только это : </span>
            <button>Все отклики</button>
            <button>Приглашения</button>
        </div>
        <hr>
        <div class="responses-list">
            <ResponseElement 
                v-for="response in responses" 
                :key="response.id" 
                :response='response' 
                v-model:showResume="dialogVisible" 
                v-model:watchResponse="watchResponse['response']" 
                v-model:watchResponseSelect="watchResponse['resume']" 
                v-model:watchResponseVacancy="watchResponse['vacancy']" 
            />
        </div>
        <DialogWindow v-model:show="dialogVisible">
            <FormSelectResume 
                v-model:show="dialogVisible"
                v-model:select="watchResponse['resume']"
                :vacancy="watchResponse['vacancy']"
                :response="watchResponse['response']"
            />
        </DialogWindow>
    </div>
</template>

<script>
import ResponseElement from '@/components/ResponseElement'
import DialogWindow from '@/components/DialogWindow'
import FormSelectResume from '@/components/FormSelectResume'
import axios from 'axios'

export default {
    name: 'Responses',
    data() {
        return {
            dialogVisible: false,
            watchResponse: {
                response: Number,
                vacancy: Number,
                resume: Number
            },
            responses: [
                {
                    id: 1111111111111111,
                    resume: {
                        id: 3,
                        name: 'backend'
                    },
                    vacancy: {
                        id: 4,
                        name: 'backend',
                        author: {
                            id: 22,
                            first_name: 'Comp'
                        }
                    },
                    status: {
                        id: 1,
                        name: 'Не просмотрен'
                    }
                },
                {
                    id: 2,
                    resume: {
                        id: 3,
                        name: 'backend'
                    },
                    vacancy: {
                        id: 4,
                        name: 'backend',
                        author: {
                            id: 22,
                            first_name: 'Comp'
                        }
                    },
                    status: {
                        id: 2,
                        name: 'Просмотрен'
                    }
                },
                {
                    id: 3,
                    resume: {
                        id: 3,
                        name: 'backend'
                    },
                    vacancy: {
                        id: 5,
                        name: 'backend',
                        author: {
                            id: 22,
                            first_name: 'Comp'
                        }
                    },
                    status: {
                        id: 3,
                        name: 'Приглашен'
                    }
                },
                {
                    id: 4,
                    resume: {
                        id: 3,
                        name: 'backend'
                    },
                    vacancy: {
                        id: 5,
                        name: 'backend',
                        author: {
                            id: 22,
                            first_name: 'Comp'
                        }
                    },
                    status: {
                        id: 4,
                        name: 'Отказ'
                    }
                },
                {
                    id: 5,
                    resume: {
                        id: 3,
                        name: 'backend'
                    },
                    vacancy: {
                        id: 5,
                        name: 'backend',
                        author: {
                            id: 22,
                            first_name: 'Comp'
                        }
                    },
                    status: {
                        id: 5,
                        name: 'В архиве'
                    }
                },
            ]
        }
    },
    components: {
        ResponseElement, DialogWindow, FormSelectResume
    },
    methods: {
        async getResponses() {
            console.log('отправил запрос');
            try {
                const response = await axios.get('http://localhost:8000/api/responses/',
                    {
                        headers: {
                            'Authorization': 'token ' + (localStorage.getItem('token'))
                        }
                    }
                )
                console.log('Hi git me responses');
                console.log(response);
            } catch (error) {
                
            }
        }
    },
    mounted() {
        console.log('Сздаем');
        this.getResponses()
    }
}
</script>

<style scoped>
.area-reponses {
    width: 1200px;
    background-color: white;
    border: 2px solid #E4E4E7;
    border-radius: 25px;
    margin: 20px auto;
    padding: 20px;
}

.responses-list {
    display: flex;
    flex-direction: column;
}


</style>