// Results.vue file
 <template>
    <div>
      <apexchart class="chart" type="bar" v-if="percentp" :options="options" :series="series"></apexchart>
      <!-- <div v-if="percentp" class="mt-3 alert alert-secondary" v-html="series"></div> -->
    </div>
  </template>

<script>
export default {
  name: "Results",
  props: ['percentp'],
  data: function() {
    return {
      options: {
        chart: {
          id: 'vuechart-example'
        },
          dataLabels: {
            enabled: true,
            formatter: function (val) {
              return val + "%";
            }
          },
          plotOptions: {
            bar: {
              columnWidth: "90%",
              dataLabels: {
                position: 'top', // top, center, bottom
              },
            }
          },               
        xaxis: {
          categories: ["A+", "A-", "B+", "B-", "C+", "C-", "D+", "D-", "E+"]
        }
      },
      series: [{
        name: 'Probabilidade',
        data: []
      }]
    }
  },
  //   computed: {
  //   chartData: function() {
  //     console.log(this.percentp)/* eslint-disable-line no-console */
  //     return this.percentp;
  //   }
  // },
    watch: {
       percentp: function(newVal) { 
         this.series = [{
           data: newVal
         }]
         console.log(this.chartData)/* eslint-disable-line no-console */
       }
    }    
};
</script>
<style>
.chart {
  max-width: 500px;
  margin: 0 auto;
}
</style>>