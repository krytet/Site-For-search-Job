<template>
    <div id="name_short_company" class="name_short_company">
        <img :src="top_company.src" alt="logo">
        <h4> {{ top_company.name }} </h4>
    </div>
</template>

<script>
export default {
    name: 'TopCompany',
    props: {
        top_company: {
            type: Object,
            requred: true
        }
    }
}
</script>

<style scoped>
    .name_short_company{
        display: flex;
        flex-direction: row;
        align-items: center;
        margin-top: 12px;
    }

    .name_short_company img {
        height: 16px;
        width: 16px;
        margin-bottom: auto;
    }

    .name_short_company h4 {
        font-size: 12px;
        margin-top: 0px;
        margin-left: 9px;
        margin-bottom: 9px;

    }
</style>