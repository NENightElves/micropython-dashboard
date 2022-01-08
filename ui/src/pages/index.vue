<template>
    <view>
        <!-- <image class="logo" src="/static/logo.png"></image>
		<view>
			<text class="title">{{title}}</text>
		</view>
		<u-action-sheet :list="list" v-model="show"></u-action-sheet> -->
        <br />
        <view style="display: flex">
            <u-input
                border="border"
                type="text"
                placeholder="请求地址"
                v-model="query_url"
            ></u-input>
            <u-button @click="change_query_url()">设置请求地址</u-button>
            <u-button @click="test_query_url()">测试</u-button>
        </view>
        <view style="display: flex">
            <u-input
                border="border"
                type="password"
                placeholder="请求密钥"
                v-model="query_password"
            ></u-input>
            <u-button @click="change_query_password()">设置请求密钥</u-button>
            <u-button @click="change_server_password()">修改请求密钥</u-button>
        </view>
        <br />
        <u-button type="info" @click="redirect('/pages/wificonfig')"
            >Wifi设置</u-button
        >
        <br />
        <u-button type="info" @click="redirect('/pages/filelist')"
            >文件管理</u-button
        >
        <br />
        <u-button type="warning" @click="query_reboot()">重启</u-button>
    </view>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            query_url: "",
            query_password: "",
        };
    },
    onLoad() {
        this.query_url = this.$axios.defaults.baseURL;
    },
    methods: {
        change_query_url: function () {
            this.$axios.defaults.baseURL = this.query_url;
            alert("设置成功！");
            // console.log(this.$axios.defaults.baseURL);
            // this.$axios
            //     .get("/test")
            //     .then((response) => {
            //         console.log(response)
            //     })
            //     .catch((err) => {
            //         console.log(err)
            //     });
            // this.$axios
            //     .post("/test")
            //     .then((response) => {
            //         console.log(response)
            //     })
            //     .catch((err) => {
            //         console.log(err)
            //     });
            // this.$axios
            //     .post("/api/systemconfig/essid")
            //     .then((response) => {
            //         console.log(response)
            //     })
            //     .catch((err) => {
            //         console.log(err)
            //     });
        },
        test_query_url: function () {
            axios
                .get(this.query_url + "/test")
                .then((response) => {
                    if (response.data["status"] == "ok") alert("测试成功！");
                    else alert("测试错误！");
                })
                .catch((err) => {
                    alert("测试错误！");
                });
        },
        change_query_password: function () {
            this.$axios.defaults.headers.post["Authorization"] =
                this.query_password;
            alert("设置成功！");
        },
        change_server_password: function () {
            this.$axios
                .post("/api/systemconfig/syspwd", {
                    Authorization: this.query_password,
                })
                .then((res) => {
                    if (res.data["status"] == "ok") alert("修改成功！");
                    else alert("修改失败！错误：" + res.data["status"]);
                })
                .catch((err) => {
                    console.log(err);
                    alert("修改失败！");
                });
        },
        query_reboot: function () {
            this.$axios
                .post("/api/reboot")
                .then((res) => {
                    if (res.data["status"] == "ok") alert("重启成功！");
                    else alert("重启失败！err：" + res.data["status"]);
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        redirect: function (url) {
            uni.navigateTo({ url: url });
        },
    },
};
</script>

<style></style>
