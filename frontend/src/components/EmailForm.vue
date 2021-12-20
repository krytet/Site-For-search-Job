<template>
    <div id="email_mailing" class="email_mailing">
        <h2>Want keep up-to-date?</h2>
        <h3>Get a daily email of all new jobs</h3>
        <input type="email" name="mailing" id="mailing" placeholder="Enter you email">
    </div>
</template>

<script>
export default {
    name: 'EmailForm',
}
</script>

<style scoped>
    .email_mailing {
        background-image: url("~@/image/Email.png");
        border-radius: 8px;
        height: 365px;
        width: 256px;
        display: flex;
        flex-direction: column;
        margin: 0px;
        vertical-align: middle;
        color: white;
        margin-top: 16px;
    }

    .email_mailing h2 {
        font-size: 24px;
        margin-top: auto;
        margin-left: 24px;
        margin-right: 24px;
        margin-bottom: 0px;
        width: 150px;
    }

    .email_mailing h3 {
        font-size: 12px;
        margin-left: 24px;
        margin-right: 24px;
        margin-bottom: 16px;
        width: 190px;
    }

    .email_mailing input {
        border-radius: 4px;
        border: 1px solid #D4D4D8;
        margin-left: 24px;
        margin-right: 24px;
        height: 40px;
        padding-left: 12px;
        margin-bottom: auto;
    }

</style>