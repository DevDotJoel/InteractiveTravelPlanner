<script>
	import SuggestionList from '$lib/components/ui/suggestion-list.svelte';
	import { superForm } from 'sveltekit-superforms';
	export let data;
	const { form, errors, constraints, message, enhance } = superForm(data.form, {
		resetForm: false
	});
</script>

<div class="row mt-3">
	<div class="col">
		<div class="card rounded-3 border-0" aria-hidden="true">
			<div class="card-body">
				<div class="row">
					<div class="col">
						<h2>
							<b>Travel Planner</b>
						</h2>
						<div class="text-muted">Select your preferences</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
{#if $message?.error}
	<div class="row mt-2">
		<div class="col">
			<span class="invalid-feedback d-block">{$message?.error}</span>
		</div>
	</div>
{/if}
<div class="row mt-3">
	<div class="col">
		<div class="card rounded-3 border-0" aria-hidden="true">
			<div class="card-body">
				<div class="row">
					<div class="col">
						<form method="POST" action="?/suggestions" use:enhance>
							<div class="row">
								<div class="col">
									<label class="text-muted" for="travelType"> Travel Type</label>
									<select
										class={`form-select rounded-3 ${$errors.travelType ? 'is-invalid' : ''}`}
										name="travelType"
										bind:value={$form.travelType}
									>
										<option value="" selected></option>
										<option value="BEACH">Beach</option>
										<option value="MOUNTAIN">Mountain</option>
										<option value="CITY">City</option>
									</select>
									{#if $errors.travelType}<span class="invalid-feedback d-block"
											>{$errors.travelType}</span
										>{/if}
								</div>
							</div>
							<div class="row mt-2">
								<div class="col">
									<label class="text-muted" for="activityType"> Activities</label>
									<select
										class={`form-select rounded-3 ${$errors.activityType?._errors ? 'is-invalid' : ''}`}
										name="activityType"
										multiple
										bind:value={$form.activityType}
									>
										<option value="ADVENTURE">Adventure</option>
										<option value="RELAXATION">Relaxation</option>
										<option value="CULTURAL">Cultural</option>
									</select>
									{#if $errors.activityType?._errors}<span class="invalid-feedback d-block"
											>{$errors.activityType._errors}</span
										>{/if}
								</div>
							</div>
							<div class="row mt-2">
								<div class="col d-flex justify-content-center">
									<div>
										<button type="submit" class="btn btn-dark rounded-5"> Get Suggestions</button>
									</div>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

{#if $message?.suggestions}
	<div class="row mt-2">
		<div class="col">
			<SuggestionList suggestions={$message?.suggestions} />
		</div>
	</div>
{/if}
