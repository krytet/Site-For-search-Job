<template>
    <div id="job_info" class="job_info">
        <div id="name_company" class="name_company">
            <img src="@/image/Avatar.png" alt="Avatar">
            <div id="name_com" class="name_com">{{ vacancy.author.first_name }}</div>
            <div id="city" class="city">• {{ vacancy.location.name }}</div>
            <div v-if="vacancy.data_age < 1" id="data_age" class="new">New</div>
            <div v-else id="data_age" class="data_age">{{ vacancy.data_age }} d</div>
        </div>
        <div id="name_job" class="name_job">
            <router-link :to="{ path: '/vacancy/' + vacancy.id}" style="text-decoration: none; color: inherit;">
                <h2>{{ vacancy.name }} {{ vacancy.salary }}</h2>
            </router-link>
        </div>
        <div id="description" class="description">
            <h3>{{ vacancy.discription }}
            </h3>
            <img v-if="vacancy.is_like" src="@/image/Like.png" alt="Like">
            <img v-else src="@/image/heart.png" alt="heart">
        </div>
    </div>
</template>

<script>
export default {
    name: 'VacancyItem',
    props: {
        vacancy: {
            type: Object,
            requred: true
        }
    },

}
</script>

<style scoped>
    .job_info {
        min-height: 100px;
        margin: 25px 24px;
        display: flex;
        flex-direction: column;
        border-bottom: 1px solid #E4E4E7;
    }
    
    .name_company {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    
    .name_company img {
        height: 32px;
        width: 32px;
    }
    
    .name_com {
        font-size: 14px;
        padding-left: 10px;
    }
    
    .city {
        flex-grow: 1;
        color: #A1A1AA;
        font-size: 12px;
        padding-left: 5px;
    }
    
    .data_age {
        color: #A1A1AA;
        font-size: 12px;
        padding-left: 5px;
    }
    
    .new {
        color: #6D28D9;
    }
    
    .name_job h2 {
        font-size: 18px;
        margin-bottom: 7px;
        text-decoration-line: none;
        text-decoration-style: none;
        transition: 5s;
        color: black;
    }

    .name_job h2:hover {
        transition: 5s;
        color: purple;
    }

    .description {
        display: flex;
        flex-direction: row;
        margin-bottom: 25px;
    }
    
    .description h3 {
        color: #71717A;
        font-size: 14px;
        flex-grow: 1;
        margin: 0px;
    }
    
    .description img {
        margin-left: 35px;
        margin-top: auto;
        margin-bottom: auto;
    }
</style>