<template>
    <view>
        <u-table>
            <u-tr>
                <u-th>文件名</u-th>
                <u-th>类型</u-th>
                <u-th>操作</u-th>
            </u-tr>
            <u-tr>
                <u-td v-if="predir != ''"
                    ><div style="color: blue" @click="redirectprev()">
                        ..
                    </div></u-td
                >
                <u-td v-if="predir != ''">d</u-td>
                <u-td v-if="predir != ''">N/A</u-td>
            </u-tr>
            <u-tr v-for="item in files" :key="item['name']">
                <u-td v-if="item.type == 'f'"
                    ><div
                        style="color: blue"
                        @click="redirectfile(item['name'])"
                    >
                        {{ item["name"] }}
                    </div></u-td
                >
                <u-td v-if="item.type == 'd'"
                    ><div
                        style="color: blue"
                        @click="redirectdir(item['name'])"
                    >
                        {{ item["name"] }}
                    </div></u-td
                >
                <u-td>{{ item["type"] }}</u-td>
                <u-td
                    ><div
                        style="color: blue"
                        @click="deletefile([item['name']])"
                    >
                        删除
                    </div></u-td
                >
            </u-tr>
        </u-table>
        <view style="display: flex">
            <u-input
                border="border"
                type="text"
                placeholder="文件名"
                v-model="create_file_name"
            ></u-input>
            <u-button @click="createfile('f')">创建文件</u-button>
            <u-button @click="createfile('d')">创建文件夹</u-button>
        </view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            files: [],
            dir: "/",
            predir: "",
            create_file_name: "",
        };
    },
    onLoad(args) {
        if (args.dir) this.dir = args.dir;
        if (this.dir != "/") {
            this.predir = this.dir.substring(0, this.dir.lastIndexOf("/"));
            if (this.predir == "") this.predir = "/";
        }
        console.log(this.dir);
        console.log(this.predir);
        this.$axios
            .post("/api/files/list", { dir: this.dir })
            .then((res) => {
                this.files = res.data["files"];
            })
            .catch((err) => {
                console.log(err);
            });
    },
    methods: {
        redirectdir: function (path) {
            let url = "";
            if (this.dir == "/") url = "/pages/filelist?dir=" + this.dir + path;
            else url = "/pages/filelist?dir=" + this.dir + "/" + path;
            uni.navigateTo({
                url: url,
            });
        },
        redirectprev: function () {
            uni.navigateTo({
                url: "/pages/filelist?dir=" + this.predir,
            });
        },
        redirectfile: function (path) {
            let url = "";
            if (this.dir == "/") url = "/pages/file?path=" + this.dir + path;
            else url = "/pages/file?path=" + this.dir + "/" + path;
            uni.navigateTo({
                url: url,
            });
        },
        createfile: function (type) {
            if (this.create_file_name != "") {
                let cfn = "";
                if (this.dir == "/") cfn = this.dir + this.create_file_name;
                else cfn = this.dir + "/" + this.create_file_name;
                this.$axios
                    .post("/api/files/create", {
                        files: [{ name: cfn, type: type }],
                    })
                    .then((res) => {
                        if (res.data["status"] == "ok") {
                            alert("创建成功！");
                            this.create_file_name = "";
                        } else alert("错误！err：" + res.data["status"]);
                        this.$axios
                            .post("/api/files/list", { dir: this.dir })
                            .then((res) => {
                                this.files = res.data["files"];
                            })
                            .catch((err) => {
                                console.log(err);
                            });
                    })
                    .catch((err) => {
                        console.log(err);
                    });
            }
        },
        deletefile: function (filenames) {
            for (let i = 0; i < filenames.length; i++)
                if (this.dir == "/") filenames[i] = this.dir + filenames[i];
                else filenames[i] = this.dir + "/" + filenames[i];
            this.$axios
                .post("api/files/delete", { files: filenames })
                .then((res) => {
                    if (res.data["status"] == "ok") {
                        alert("删除成功！");
                    } else alert("错误！err：" + res.data["status"]);
                    this.$axios
                        .post("/api/files/list", { dir: this.dir })
                        .then((res) => {
                            this.files = res.data["files"];
                        })
                        .catch((err) => {
                            console.log(err);
                        });
                })
                .catch((err) => {
                    console.log(err);
                });
        },
    },
};
</script>

<style></style>
