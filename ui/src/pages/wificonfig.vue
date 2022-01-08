<template>
    <view>
        <br />
        <u-input
            border="border"
            type="text"
            placeholder="essid"
            v-model="essid"
        ></u-input>
        <br />
        <u-input
            border="border"
            type="password"
            placeholder="password"
            v-model="password"
        ></u-input>
        <br />
        <u-input
            border="border"
            type="text"
            placeholder="IP"
            v-model="ip"
        ></u-input>
        <br />
        <u-input
            border="border"
            type="text"
            placeholder="mask"
            v-model="mask"
        ></u-input>
        <br />
        <u-input
            border="border"
            type="text"
            placeholder="gateway"
            v-model="gateway"
        ></u-input>
        <br />
        <u-input
            border="border"
            type="text"
            placeholder="DNS"
            v-model="dns"
        ></u-input>
        <br />
        <u-button type="primary" @click="change_wifi">提交</u-button>
    </view>
</template>

<script>
export default {
    data() {
        return {
            essid: "",
            password: "",
            ip: "",
            mask: "",
            gateway: "",
            dns: "",
        };
    },
    onLoad() {
        this.$axios
            .post("/api/systemconfig/essid")
            .then((res) => {
                if (res.data["status"] == "ok") this.essid = res.data["essid"];
                else alert(res.data["status"]);
            })
            .catch((err) => {
                console.log(err);
            });
    },
    methods: {
        change_wifi: function () {
            let r = {};
            if (this.essid == "") {
                alert("修改失败，wifi名称为空！");
                return;
            }
            r["essid"] = this.essid;
            r["password"] = this.password;
            if (
                this.ip != "" &&
                this.mask != "" &&
                this.gateway != "" &&
                this.dns != ""
            ) {
                r["static"] = {};
                r["static"]["ip"] = this.ip;
                r["static"]["subnet"] = this.mask;
                r["static"]["gateway"] = this.gateway;
                r["static"]["dns"] = this.dns;
            }
            this.$axios
                .post("/api/systemconfig/changewifi", r)
                .then((res) => {
                    if (res.data["status"] == "ok") alert("修改成功！PYBOARD正在重启...");
                    else alert("修改失败！错误：" + res.data["status"]);
                })
                .catch((err) => {
                    console.log(err);
                    alert("修改失败！");
                });
        },
    },
};
</script>

<style></style>
