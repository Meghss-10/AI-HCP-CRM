import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  hcp_name: "",
  interaction_type: "Meeting",
  interaction_date: "",
  interaction_time: "",
  attendees: "",
  topics_discussed: "",
  materials_shared: "",
  samples_distributed: "",
  sentiment: "",
  outcomes: "",
  follow_up: "",
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    updateInteraction: (state, action) => {
      console.log("Reducer Payload:", action.payload);

      return {
        ...state,
        ...action.payload,
      };
    },

    clearInteraction: () => ({
      ...initialState,
    }),
  },
});

export const {
  updateInteraction,
  clearInteraction,
} = interactionSlice.actions;

export default interactionSlice.reducer;