new Vue({
    el:"#app",

    data:{
        monedas:{},
        cantidad: 0,
        from: "EUR",
        to: "USD",
        result: 0

    },
    mounted(){
        this.getMonedas()
    },
    computed:{
        formatearMonedas(){
            return Object.values(this.monedas);
        },
        calcularResultado(){
            return(Number(this.cantidad) * this.result).toFixed(3);
        },
        deshabilidado(){
            return this.cantidad ===0 || !this.cantidad;
        }
    },
    methods:{
        getMonedas(){
            const monedas = localStorage.getItem("monedas");

            if(monedas){
                this.monedas =JSON.parse(monedas);
                return;
            }

            axios.get("https://free.currconv.com/api/v7/currencies?apiKey=dec3e8cd3f56fcdab3a5")
            .then(response => {
                this.monedas = response.data.results;
                localStorage.setItem("monedas", JSON.stringify(response.data.results));
                console.log(response);
        });
        },
        convertirMoneda(){
            const busqueda = `${this.from}_${this.to}`;
            axios.get(`https://free.currconv.com/api/v7/convert?q=${busqueda}&apiKey=dec3e8cd3f56fcdab3a5`)

            .then((response) => {
                console.log(response)
                this.result = response.data.results[busqueda].val;
            });
        }
    },
    watch:{
        from(){
            this.result =0;
        },
        to(){
            this.result = 0;
        }
    }
});




