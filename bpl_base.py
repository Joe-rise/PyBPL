import numpy as np


class BPLBase(object):
    """
    BPL base class.
    """

    def __init__(self,
                 cpd,
                 ordered=True,
                 add_variance=True):
        """
        :param cpd:
         A CPD instance (from cpd.py).
        :param ordered
         Bool: whether or not this BPL uses ordered construction, e.g. handwriting composition.
        :return:
        """
        self.cpd = cpd
        self.ordered = ordered
        self.add_variance = add_variance

    def generate_type(self):
        """
        Forward model to generate a type given a Program instance.

        :return:
          genera_token function handle
        """
        type_params = {'num_parts': self.sample_number_parts(), 'relatons': [], 'strokes': []}
        for i in xrange(type_params['num_parts']):
            num_subparts = self.sample_number_subparts()
            type_params['strokes'].append([])
            for j in xrange(num_subparts):
                type_params['strokes'][i][j] = self.sample_subpart_sequence(type_params)
            type_params['relations'].append(self.sample_relations(type_params))

        def generate_token(type_params):
            # TODO: generalize. Trajectories, locations are specific to motor programs and spatial cases
            trajectories = []
            locations = []
            for part in xrange(type_params['num_parts']):
                if self.add_variance:
                    # TODO: generalize. Strokes are specific to handwriting case.
                    type_params['strokes'][part] = self.sample_variance(type_params['strokes'][part])
                locations.append(self.sample_start_location(type_params, part))
                trajectories.append(self.compose_trajectory(type_params, part))
            affine = self.sample_affine_transform()
            type_params['locations'] = locations
            type_params['trajectories'] = trajectories
            image = self.sample_image(type_params, affine)
            return image

        return generate_token

    def sample_number_parts(self):
        # TODO: generic sampler - maybe pluggable for more flexibility?
        return 0

    def sample_number_subparts(self):
        # TODO: generic sampler - maybe pluggable for more flexibility?
        # different samplers will depend highly on use case
        return 0

    def sample_subpart_sequence(self, type_params):
        #TODO: sample subpart sequence based on type_params
        return 0

    def sample_relations(self, type_params):
        #TODO: sample relations based on type_params
        # In some use cases relations may take on a different meaning; relations types will need to have well-defined
        # behavior
        return 0

    def sample_variance(self, stroke_part):
        # TODO: move from no-op to sample variance
        return stroke_part

    def sample_start_location(self, type_params, num):
        #TODO: sample start location from info in type_params
        return 0

    def compose_trajectory(self, type_params, num):
        #TODO: compose full trajectory, assuming ordered construction
        return 0

    def sample_affine_transform(self):
        #TODO: sample affine transform
        return 0

    def sample_image(self, type_params, affine):
        #TODO: sample image from type
        return 0
