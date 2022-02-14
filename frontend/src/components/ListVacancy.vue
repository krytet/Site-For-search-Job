<template>
    <div id="jobs_block" class="jobs_block">
        <div id="search" class="search">
            <img src="@/image/search.png" alt="search">
            <input type="text" name="search" id="input_search" placeholder="Start searching...">
            <!--<div id="sort" class="sort">Сортировать:</div>-->
            <div id="sort" class="sort">
                <SelectForList
                    v-model="SelectedSort"
                    :options="sortOptions"
                    @change="ChangeSortOption"
                />
            </div>
        </div>
        <div id="jobs_list" class="jobs_list" v-if="vacancies.length > 0">
            <h6 class="count-vacancy"> Найдено {{ vacanciesCount }} вакансий </h6>
            <VacancyItem v-for="vacancy in vacancies" :vacancy="vacancy" :key="vacancy.id" />
        </div>
    </div>
</template>

<script>
import VacancyItem from '@/components/VacancyItem'
import SelectForList from '@/components/elements/SelectForList'

export default {
    name: 'ListVacancy',
    data() {
        return {
            dialogSortVisivle: false,
            SelectedSort: '',
            sortOptions: [
                {value: '-id', name: 'По дате'},
                {value: '-salary', name: 'По убыванию зарплат'},
                {value: 'salary', name: 'По возрастанию зарплат'}
            ],
        }
    },
    props: {
        modelValue: {
            type: String,
        },
        vacancies: {
            type: Array,
            requred: true
        },
        vacanciesCount: {
            type: Number
        }
    },
    components: {
        VacancyItem, SelectForList
    },
    methods: {
        ChangeSortOption(event) {
            this.$emit('update:modelValue', event.target.value)
        }
    }

}
</script>

<style scoped>
    .jobs_block {
        background-color: white;
        border: 2px solid #E4E4E7;
        border-radius: 4px;
    }
    
    .search {
        display: flex;
        flex-direction: row;
        padding: 16px 20px;
        border-bottom: 2px solid #E4E4E7;
    }
    
    .search input {
        flex-grow: 1;
        color:  #71717A;
        border: none;
        margin-left: 16px;
    }

    input:focus {
        border: none;
        outline: none;
    }
    
    input::placeholder {
        color: #D4D4D8; 
    }
    
    .sort {
        color: #71717A;
    }

    .count-vacancy {
        font-size: 12px;
        color: #71717A;
        margin: 4px auto;
        text-align: center;
    }
</style>