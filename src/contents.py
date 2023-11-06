from pyscript import Element


class Timogen:
    def labelized_field(label: str):
        return f"""
        <div class="mb-3 d-flex flex-wrap">
            <label class="col-12 col-sm-4 col-md-3 col-lg-2 col-form-label">
                {label}
            </label>
            <div class="col">
                <slot></slot>
            </div>
            <br />
            <br />
        </div>
    """

class Therapist(Timogen):
    """
    <LabelizedField for="therapist_name" label="Nom">
      <!-- There is no ID because I do not want autofill on this field -->
      <multiselect v-model="therapistSelected" :options="therapistList" selectLabel="↵" selectedLabel="" deselectLabel="×"
        @search-change="retrieveTherapists" @open="retrieveTherapists" @input="updateSelected"
        placeholder="Commencez à écrire..." label="name" track-by="id">
        <template slot="noOptions"> ... </template>
        <template slot="noResult"> Pas de résultats. </template>
      </multiselect>
    </LabelizedField>

    <!-- Address -->
    <LabelizedField for="therapist_address" label="Adresse">
      <textarea id="therapist_address" name="therapist_address" rows="2" cols="50" maxlength="200" type="address"
        class="form-control" placeholder="" v-model="address" />
    </LabelizedField>

    <!-- inami -->
    <LabelizedField for="therapist_inami" label="Numéro INAMI">
      <input id="therapist_inami" name="therapist_inami" type="inami" class="form-control" placeholder="0-0000000-000"
        v-model="inami_nb" maxlength="13" />
    </LabelizedField>

    <!-- BCE -->
    <LabelizedField for="therapist_bce" label="BCE">
      <input id="therapist_bce" name="therapist_bce" type="bce" class="form-control" placeholder="0000.000.000"
        v-model="bce" maxlength="12" />
    </LabelizedField>

    <!-- Bank -->
    <LabelizedField for="therapist_ba" label="Numéro de compte">
      <input id="therapist_ba" name="therapist_ba" type="bank_account" class="form-control"
        placeholder="BE40 XXXX XXXX XXXX" v-model="bank_account" maxlength="19" />
    </LabelizedField>

    <!-- contracted -->
    <LabelizedField for="contracted" label="Conventionné">
      <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" v-model="contracted" id="contracted" />
      </div>
    </LabelizedField>
    """
    pass

def therapist_name_change():
    manual_div = Element("therapist_name")
    print(manual_div.element.innerHTML)
