import requests
import json
 
user = input("Enter Your Username : ")
pas = input("Enter Your password : ")



Access = requests.post("https://api.twitter.com/oauth2/token", data= "grant_type=client_credentials", headers = {
  'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+10+Pro;Redmi;begonia;0;;0;2016)",
  'Accept': "application/json",
  'Accept-Encoding': "br, gzip, deflate",
  'Content-Type': "application/x-www-form-urlencoded",
  'timezone': "Asia/Aden",
  'os-security-patch-level': "2022-04-01",
  'optimize-body': "true",
  'x-twitter-client': "TwitterAndroid",
  'x-attest-token': "no_token",
  'x-twitter-client-adid': "20d041fe-7911-446c-9a92-035ed8ab0904",
  'x-twitter-client-language': "ar-EG",
  'x-client-uuid': "7032db5b-591f-4f73-842b-2f9e52516871",
  'x-twitter-client-deviceid': "137d1fbe27f7dc2d",
  'authorization': "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw==",
  'x-twitter-client-version': "10.68.1-release.0",
  'cache-control': "no-store",
  'x-twitter-active-user': "no",
  'x-twitter-api-version': "5",
  'x-twitter-client-limit-ad-tracking': "0",
  'x-b3-traceid': "dbffbe7a8d609493",
  'accept-language': "ar-EG",
  'x-twitter-client-flavor': ""
}).json()["access_token"]

headers = {
  'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+8+Pro;Redmi;begonia;0;;0;2016)",
  'Accept': "application/json",  
  'Content-Type': "application/json", 
  'authorization': f"Bearer {Access}", 
  'system-user-agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
}


gs = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers).json()["guest_token"]
headers.update({'x-guest-token': gs})

response = requests.post("https://api.twitter.com/1.1/onboarding/task.json", params = {
  'flow_name': "login",
  'api_version': "1",
  'known_device_token': "",
  'sim_country_code': "ye"
}, data=json.dumps({
  "input_flow_data": {
    "country_code": None,
    "flow_context": {
      "referrer_context": {
        "referral_details": "utm_source=google-play&utm_medium=organic",
        "referrer_url": ""
      },
      "start_location": {
        "location": "splash_screen"
      }
    },
    "requested_variant": None,
    "target_user_id": 0
  },
  "subtask_versions": {
    "generic_urt": 3,
    "standard": 1,
    "open_home_timeline": 1,
    "app_locale_update": 1,
    "enter_date": 1,
    "email_verification": 3,
    "deregister_device": 1,
    "enter_password": 5,
    "enter_text": 6,
    "one_tap": 2,
    "cta": 7,
    "single_sign_on": 1,
    "fetch_persisted_data": 1,
    "enter_username": 3,
    "web_modal": 2,
    "fetch_temporary_password": 1,
    "menu_dialog": 1,
    "sign_up_review": 5,
    "user_recommendations_urt": 3,
    "in_app_notification": 1,
    "sign_up": 2,
    "typeahead_search": 1,
    "app_attestation": 1,
    "user_recommendations_list": 4,
    "cta_inline": 1,
    "contacts_live_sync_permission_prompt": 3,
    "choice_selection": 5,
    "js_instrumentation": 1,
    "alert_dialog_suppress_client_events": 1,
    "privacy_options": 1,
    "topics_selector": 1,
    "wait_spinner": 3,
    "tweet_selection_urt": 1,
    "end_flow": 1,
    "settings_list": 7,
    "open_external_link": 1,
    "phone_verification": 5,
    "security_key": 3,
    "select_banner": 2,
    "upload_media": 1,
    "web": 2,
    "alert_dialog": 1,
    "open_account": 2,
    "passkey": 1,
    "action_list": 2,
    "enter_phone": 2,
    "open_link": 1,
    "show_code": 1,
    "update_users": 1,
    "check_logged_in_account": 1,
    "enter_email": 2,
    "select_avatar": 4,
    "location_permission_prompt": 2,
    "notifications_permission_prompt": 4
  }
}), headers=headers)
AT = (response.headers)['att']


tok = response.json()["flow_token"]

headers.update({'att': AT})



res = requests.post("https://api.twitter.com/1.1/onboarding/task.json", data=json.dumps({
  "flow_token": tok,
  "subtask_inputs": [
    {
      "enter_text": {
        "challenge_response": None,
        "suggestion_id": None,
        "text": user,
        "link": "next_link"
      },
      "subtask_id": "LoginEnterUserIdentifier"
    }
  ],
  "subtask_versions": {
    "generic_urt": 3,
    "standard": 1,
    "open_home_timeline": 1,
    "app_locale_update": 1,
    "enter_date": 1,
    "email_verification": 3,
    "deregister_device": 1,
    "enter_password": 5,
    "enter_text": 6,
    "one_tap": 2,
    "cta": 7,
    "single_sign_on": 1,
    "fetch_persisted_data": 1,
    "enter_username": 3,
    "web_modal": 2,
    "fetch_temporary_password": 1,
    "menu_dialog": 1,
    "sign_up_review": 5,
    "user_recommendations_urt": 3,
    "in_app_notification": 1,
    "sign_up": 2,
    "typeahead_search": 1,
    "app_attestation": 1,
    "user_recommendations_list": 4,
    "cta_inline": 1,
    "contacts_live_sync_permission_prompt": 3,
    "choice_selection": 5,
    "js_instrumentation": 1,
    "alert_dialog_suppress_client_events": 1,
    "privacy_options": 1,
    "topics_selector": 1,
    "wait_spinner": 3,
    "tweet_selection_urt": 1,
    "end_flow": 1,
    "settings_list": 7,
    "open_external_link": 1,
    "phone_verification": 5,
    "security_key": 3,
    "select_banner": 2,
    "upload_media": 1,
    "web": 2,
    "alert_dialog": 1,
    "open_account": 2,
    "passkey": 1,
    "action_list": 2,
    "enter_phone": 2,
    "open_link": 1,
    "show_code": 1,
    "update_users": 1,
    "check_logged_in_account": 1,
    "enter_email": 2,
    "select_avatar": 4,
    "location_permission_prompt": 2,
    "notifications_permission_prompt": 4
  }
}), headers=headers)

tok2 = res.json()["flow_token"]

req = requests.post("https://api.twitter.com/1.1/onboarding/task.json", data=json.dumps({
  "flow_token": tok2,
  "subtask_inputs": [
    {
      "enter_password": {
        "password": pas,
        "link": "next_link"
      },
      "subtask_id": "LoginEnterPassword"
    }
  ],
  "subtask_versions": {
    "generic_urt": 3,
    "standard": 1,
    "open_home_timeline": 1,
    "app_locale_update": 1,
    "enter_date": 1,
    "email_verification": 3,
    "deregister_device": 1,
    "enter_password": 5,
    "enter_text": 6,
    "one_tap": 2,
    "cta": 7,
    "single_sign_on": 1,
    "fetch_persisted_data": 1,
    "enter_username": 3,
    "web_modal": 2,
    "fetch_temporary_password": 1,
    "menu_dialog": 1,
    "sign_up_review": 5,
    "user_recommendations_urt": 3,
    "in_app_notification": 1,
    "sign_up": 2,
    "typeahead_search": 1,
    "app_attestation": 1,
    "user_recommendations_list": 4,
    "cta_inline": 1,
    "contacts_live_sync_permission_prompt": 3,
    "choice_selection": 5,
    "js_instrumentation": 1,
    "alert_dialog_suppress_client_events": 1,
    "privacy_options": 1,
    "topics_selector": 1,
    "wait_spinner": 3,
    "tweet_selection_urt": 1,
    "end_flow": 1,
    "settings_list": 7,
    "open_external_link": 1,
    "phone_verification": 5,
    "security_key": 3,
    "select_banner": 2,
    "upload_media": 1,
    "web": 2,
    "alert_dialog": 1,
    "open_account": 2,
    "passkey": 1,
    "action_list": 2,
    "enter_phone": 2,
    "open_link": 1,
    "show_code": 1,
    "update_users": 1,
    "check_logged_in_account": 1,
    "enter_email": 2,
    "select_avatar": 4,
    "location_permission_prompt": 2,
    "notifications_permission_prompt": 4
  }
}), headers=headers)

print(req.text)
