<template>
<div>
    <home_header/>
    <content_1/>
    <home_footer/>
</div>
</template>

<script>
import home_header from '@/components/home_header.vue'
import content_1 from '@/components/content_1.vue'
import home_footer from '@/components/home_footer.vue'


export default {
    components: {
        home_header,
        content_1,
        home_footer
    }
}
</script>

<style lang="less" scoped>

</style>