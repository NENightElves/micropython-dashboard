<template>
    <view>
        <br />
        <u-input border="border" type="textarea" v-model="content"></u-input>
        <u-button type="primary" @click="submit()">提交</u-button>
    </view>
</template>

<script>
export default {
    data() {
        return {
            path: "",
            content: "",
        };
    },
    onLoad(args) {
        this.path = args["path"];
        this.$axios
            .post("/api/files/get", { file: this.path })
            .then((res) => {
                if (res.data["status"] == "ok")
                    this.content = res.data["content"];
                else alert("错误！err：" + res.data["status"]);
            })
            .catch((err) => {
                console.log(err);
            });
    },
    methods: {
        submit: function () {
            this.$axios
                .post("/api/files/modify", {
                    file: this.path,
                    content: this.content,
                })
                .then((res) => {
                    if (res.data["status"] == "ok") alert("修改成功！");
                    else alert("错误！err：" + res.data["status"]);
                })
                .catch((err) => {
                    console.log(err);
                });
        },
    },
};
</script>

<style></style>
