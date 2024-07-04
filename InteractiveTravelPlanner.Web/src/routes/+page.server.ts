import {
	ActivityType,
	TravelType,
	type TravelPreferenceModel
} from '$lib/models/TravelPreferencesModel';
import { fail, message, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { z } from 'zod';

const activities = ['ADVENTURE', 'RELAXATION', 'CULTURAL'] as const;
const activitiesSchema = z
	.enum(activities)
	.array()
	.refine(
		(array) => {
			return array.some((item) => activities.includes(item));
		},
		{
			message: `Activities must contain at least one of the following: ${activities.join(', ')}`
		}
	);
const schema = z.object({
	travelType: z.string().min(1, {
		message: `Travel type must  be one of the following: Beach,Mountain,City`
	}),
	activityType: activitiesSchema
});

export const load = async () => {
	const form = await superValidate(zod(schema));

	return { form };
};
/** @type {import('./$types').Actions} */
export const actions = {
	suggestions: async ({ request }) => {
		const form = await superValidate(request, zod(schema));
		console.log(form);
		if (!form.valid) {
			// Again, return { form } and things will just work.
			return fail(400, { form });
		}

		const preference: TravelPreferenceModel = {
			travel_type: TravelType[form.data.travelType as keyof typeof TravelType],
			activities: form.data.activityType.map(
				(activity) => ActivityType[activity as keyof typeof ActivityType]
			)
		};
		try {
			const res = await fetch('http://127.0.0.1:8000/api/travel/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(preference)
			});
			const data = await res.json();
			return message(form, {
				suggestions: data
			});
		} catch (error) {
			return fail(400, { form });
		}
	}
};
