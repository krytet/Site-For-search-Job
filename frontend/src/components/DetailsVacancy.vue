<template>
    <div class="view-detail-vacancy">
        <h1> {{ detail.name }} </h1>
        <h2 v-if="detail.salary == none">з/п не указана </h2>
        <h2 v-else class="gray"> {{ detail.salary }} руб.</h2>
        <h3>Требуемые навыки</h3>
        <div class="list-skills" >
            <span v-for="skill in detail.skills" :key="skill.id"> {{ skill.name }} </span>
        </div>
        <h2>Описание вакансии</h2>
        <p>Обязанности:</p>
        <p>- Разработка новых проектов;</p>
        <p>- Поддержка и развитие существующих проектов.</p>
        <p>Требования:</p>
        <p>Ты позитивен и коммуникабелен</p>
        <p>У тебя отличные навыки разработки на Python и Django;</p>
        <p>Хорошо умеешь и имел опыт написания unit-тестов;</p>
        <p>Ты готов предлагать архитектурные решения, активное участие в проектировании архитектуры продукта;</p>
        <p>Опыт работы с микросервисной архитектурой;</p>
        <p>Имеешь опыт коммерческой разработки на Python не менее 2 лет;</p>
        
    </div>
    <div id="company-info-and-skills" class="company-info-and-skills">
        <h3> {{ detail.author.first_name }} </h3>
        <img src="https://w7.pngwing.com/pngs/179/878/png-transparent-computer-icons-eagle-emblem-animals-logo.png" alt="logo">
        <!--<img :src="detail.image" alt="logo">-->
        <h5> {{ detail.location.name }} </h5>
        <p><a href="#" class="response-vacancy">Откликнуться</a></p>
        <h3>Условия работы у нас:</h3>
        <div class="requirements-list-for-job">
            <p>Опыт работы: <span> {{ detail.experience.name }} </span></p>
            <p>Тип занятости: <span> {{ detail.type_employment.name }} </span></p>
            <p>График работы: <span> {{ detail.work_schedule.name }} </span></p>
            <p>Образование: <span> {{ detail.education.name }} </span></p>
            <p>Удалено работать: 
                <span v-if="detail.remote_work">Можно</span>
                <span v-else>Нельзя</span>
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DetailsVacancy',
    props: {
        detail: {
            type: Object,
            requred: true
        }
    }
}
</script>

<style scoped>
    .view-detail-vacancy {
        grid-area: 'left';
        width: 700px;
        vertical-align: top;
        min-height: 1px;
        padding-left: 15px;
        padding-right: 15px;
        border: 1px dotted #939;
    
        background-color: white;
        border: 2px solid #E4E4E7;
        border-radius: 10px;
    }
    
    .view-detail-vacancy h1 {
        text-align: center;
    }
    
    .view-detail-vacancy h2 {
        text-align: center;
    }
    
    .view-detail-vacancy h3 {
        text-align: center;
    }
    
    .view-detail-vacancy h2 {
        color: #71717a7c;
    }

    .view-detail-vacancy h2.gray {
        color: #00000098;
    }
    
    .view-detail-vacancy .list-skills {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    
    .list-skills span {
        background-color: rgb(202, 138, 218);
        border: 1px solid #E4E4E7;
        border-radius: 10px;
        padding: 5px;
        margin: 5px;
    }
    
    /* Блок вывода информации о комании */
    .company-info-and-skills {
        width: 300px;
        color: #18181B;
        font-size: 16px;
        margin-bottom: 12px;
        align-items: center;
        align-self:center;
        align-content: center;
        text-align: center;
    }

    .company-info-and-skills img {
        max-width: 300px;
    }
    
    .response-vacancy {
        background-color: rgb(202, 138, 218);
        border: 1px solid #E4E4E7;
        border-radius: 5px;
        text-decoration: none;
        padding: 10px;
        color: black;
        margin: 10px;
    
    }
    .response-vacancy:hover { 
        text-decoration: none;
        color: #F3F4F6;
        transition: 0.5s;
    }
    
    .requirements-list-for-job {
        font-size: 14px;
        color: #71717a;
    }
    
    .requirements-list-for-job span {
        color: black;
        font-size: 14px;
        font-style: italic;
    }
</style>