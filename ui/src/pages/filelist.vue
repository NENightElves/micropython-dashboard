<template>
    <view>
        <u-table>
            <u-tr>
                <u-th>文件名</u-th>
                <u-th>类型</u-th>
            </u-tr>
            <u-tr>
                <u-td v-if="predir != ''"
                    ><div @click="redirectprev()">..</div></u-td
                >
                <u-td v-if="predir != ''">d</u-td>
            </u-tr>
            <u-tr v-for="item in files" :key="item['name']">
                <u-td v-if="item.type == 'f'"
                    ><div>{{ item["name"] }}</div></u-td
                >
                <u-td v-if="item.type == 'd'"
                    ><div @click="redirectdir(item['name'])">
                        {{ item["name"] }}
                    </div></u-td
                >
                <u-td>{{ item["type"] }}</u-td>
            </u-tr>
        </u-table>
    </view>
</template>

<script>
export default {
    data() {
        return {
            files: [],
            dir: "/",
            predir: "",
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
            if (this.dir == "/")
                url = "/pages/filelist?dir=" + this.dir + path;
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
    },
};
</script>

<style></style>
