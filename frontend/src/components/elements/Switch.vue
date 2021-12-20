<template>
    <label class="select_bolean">
        <input type="checkbox" :name="element.value" class="checkbox_bolean">
        <span class="check_bolean"></span>
        <span class="text"> {{ element.name }} </span>
    </label>
</template>

<script>
export default {
    name: 'Switch',
    props: {
        element: {
            type: Object
        }
    }

}
</script>

<style scoped>
    .select_bolean  {
        display: inline;
    }

    .select_bolean .text {
        position:absolute;
        padding-left: 12px;
        color: #71717A;
        vertical-align: middle;
    }

    .checkbox_bolean {
        display: none;
    }

    .check_bolean {
        display: inline-block;
        height: 16px;
        width: 28px;
        border-radius: 8px;
        background-color: #7C3AED;
        transition: 1s;
    }

    .check_bolean::before {
        content: "";
        display: block;
        position: relative;
        height: 16px;
        width: 16px;
        border-radius: 50%;
        background-color: #E4E4E7;
        left: 0%;
        opacity: 1;
        transition: 1s;
    }

    .checkbox_bolean:checked + .check_bolean::before {
        background-color: #7C3AED;
        left: 12px;
    }

    .checkbox_bolean:checked + .check_bolean {
        background-color: #E4E4E7;
    }
</style>