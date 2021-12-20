<template>
    <div id="right_sidebar" class="right_sidebar">
        <h5>Лучшие компании</h5>
        <div id="top_company_list" class="top_company_list">
            <TopCompany v-for="top_company in top_companies" :top_company="top_company" />
        </div>
        <EmailForm />
    </div>
</template>

<script>
import TopCompany from '@/components/TopCompany'
import EmailForm from '@/components/EmailForm'

export default {
    name: 'RightTopCompany',
    props: {
        top_companies: {
            type: Array,
            requred: true
        }
    },
    components: {
        TopCompany,
        EmailForm
    }
}
</script>

<style>
    .right_sidebar {
        display: flex;
        flex-direction: column;
        min-width: 256px;
    }

    .right_sidebar h5 {
        font-size: 16px;
        margin: 5px;
    }
</style>