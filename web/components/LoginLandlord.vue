<template>
  <div class="card">
    <div class="card-body">
      <h4 class="card-title">Login as Landlord</h4>
      <form class="forms-sample" v-if="!otpSent">
        <div class="form-group">
          <label for="exampleInputEmail1">Aadhar Number</label>
          <input type="number" class="form-control" id="exampleInputEmail1" placeholder="Aadhar Number" v-model="aadhar">
        </div>
        <button type="submit" class="btn btn-primary me-2" v-on:click.prevent = "sendOtp();">Send OTP</button>
      </form>
      <div v-if="otpSent">
          <hr>
          <div class="card-title">Submit OTP</div>
            <div class="card-description">We have sent you OTP to registered mobile number. Enter below to proceed.</div>
            <div class="form-group">
                <input type="text" class="form-control form-control-lg" placeholder="123456" aria-label="123456" v-model="inputOtp">
            </div>
            <button type="button" class="btn btn-primary btn-block" v-on:click.prevent="verifyOtp()">
                Submit
            </button>
      </div>
    </div>
  </div>
</template>

<script>
import loginLandlord from "@/functions/loginLandlord.js"
import verifyLoginLandlordOtp from "@/functions/verifyLoginLandlordOtp.js"

export default {
    data() {
        return {
            otpSent: false,
            aadhar: "",
            b_aadhar: "",
            isLoading: false,
            txnId: "",
            inputOtp: ""
        }
    },
    methods: {
        async sendOtp(){
            if(this.isLoading) return;
            this.isLoading = true;
            const [status, response] = await loginLandlord(this.aadhar, this);
            if(!status) alert(response);
            else{
                this.otpSent = true;
                this.txnId = response;
            }
            this.isLoading = false;
        },
        async verifyOtp(){
            if(this.isLoading) return;
            this.isLoading = true;
            const [status, response] = await verifyLoginLandlordOtp(this.txnId, this.aadhar, this.inputOtp, this)
            if(!status) alert(response);
            else {
                this.$router.push('/landlord');
            }
            this.isLoading = false;
        }
    }
}
</script>

<style>

</style>